from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages

from .models import User, Category, Listing, Comment, Bid


def index(request):
    activeListings = Listing.objects.filter(is_active=True)
    allcategories = Category.objects.all
    return render(request, "auctions/index.html", {
        "Listings": activeListings,
        "categories": allcategories
    })

def createListing(request):
    if request.method == "GET":
        allcategories = Category.objects.all
        return render(request, "auctions/create.html", {
            "categories": allcategories
        })
    else:
        title = request.POST["title"]
        description = request.POST["description"]
        if request.POST["imageurl"] != None:
            imageurl = request.POST["imageurl"]
        price = request.POST["price"]
        category = request.POST["category"]
        currentUser = request.user
        categoryData = Category.objects.get(categoryName=category)
        bid = Bid(bid= float(price), user=currentUser)
        bid.save()
        NewListing = Listing(
            title = title,
            description = description,
            imageurl = imageurl,
            price = bid,
            category = categoryData,
            owner = currentUser
        )
        NewListing.save()
        return HttpResponseRedirect(reverse(index))

def listing(request, id):
    listingData = Listing.objects.get(pk=id)
    isListingInWatchlist = request.user in listingData.watchlist.all()
    allComments = Comment.objects.filter(listing=listingData)
    isOwner = request.user.username == listingData.owner.username
    return render(request, "auctions/listing.html", {
        "listing": listingData,
        "isListingInWatchlist": isListingInWatchlist,
        "allComments": allComments,
        "isOwner": isOwner
    })

def displayCategory(request):
    if request.method == "POST":
        categoryFromForm = request.POST['category']
        category = Category.objects.get(categoryName=categoryFromForm)
        activeListings = Listing.objects.filter(is_active=True, category=category)
        allcategories = Category.objects.all
        return render(request, "auctions/index.html", {
            "Listings": activeListings,
            "categories": allcategories
        })

def removeWatchlist(request, id):
    listingData = Listing.objects.get(pk=id)
    currentUser = request.user
    listingData.watchlist.remove(currentUser)
    return HttpResponseRedirect(reverse("listing", args=(id,)))

def addWatchlist(request, id):
    listingData = Listing.objects.get(pk=id)
    currentUser= request.user
    listingData.watchlist.add(currentUser)
    return HttpResponseRedirect(reverse("listing", args=(id,)))

def displayWatchlist(request):
    currentUser = request.user
    listings = currentUser.listingWatchlist.all()
    return render(request, "auctions/watchlist.html",{
        "listings": listings
    })

def addComment(request, id):
    message = request.POST['newComment']
    listingData = Listing.objects.get(pk=id)
    isListingInWatchlist = request.user in listingData.watchlist.all()
    allComments = Comment.objects.filter(listing=listingData)
    currentUser = request.user
    isOwner = request.user.username == listingData.owner.username

    if message == '':
        return render(request, "auctions/listing.html",{
            "listing": listingData,
            "message": "Comment can not be empty!",
            "update": False,
            "isOwner": isOwner,
            "isListingInWatchlist": isListingInWatchlist,
            "allComments": allComments
        })
    else:
        newComment = Comment(
        author = currentUser,
        listing = listingData,
        message = message
        )

        newComment.save()

        return render(request, "auctions/listing.html",{
            "listing": listingData,
            "message": "Comment is posted!",
            "update": True,
            "isOwner": isOwner,
            "isListingInWatchlist": isListingInWatchlist,
            "allComments": allComments
        })

def addBid(request, id):
    newBid = request.POST['newBid']
    listingData = Listing.objects.get(pk=id)
    isListingInWatchlist = request.user in listingData.watchlist.all()
    allComments = Comment.objects.filter(listing=listingData)
    isOwner = request.user.username == listingData.owner.username
    if newBid is '':
        return render(request, "auctions/listing.html",{
            "listing": listingData,
            "message": "Bid was not updated! Please provide a valid amount",
            "update": False,
            "isOwner": isOwner,
            "isListingInWatchlist": isListingInWatchlist,
            "allComments": allComments
        })
    elif float(newBid) > listingData.price.bid:
        updateBid = Bid(user= request.user, bid=float(newBid))
        updateBid.save()
        listingData.price = updateBid
        listingData.save()
        return render(request, "auctions/listing.html",{
            "listing": listingData,
            "message": "Bid was succefully updated!",
            "update": True,
            "isOwner": isOwner,
            "isListingInWatchlist": isListingInWatchlist,
            "allComments": allComments
        })
    else:
        return render(request, "auctions/listing.html",{
            "listing": listingData,
            "message": "Bid was not updated!",
            "update": False,
            "isOwner": isOwner,
            "isListingInWatchlist": isListingInWatchlist,
            "allComments": allComments
        })

def closeAuction(request, id):
    listingData = Listing.objects.get(pk=id)
    listingData.is_active = False
    listingData.save()
    isOwner = request.user.username == listingData.owner.username
    isListingInWatchlist = request.user in listingData.watchlist.all()
    allComments = Comment.objects.filter(listing=listingData)
    return render(request, "auctions/listing.html", {
        "listing": listingData,
        "message": "The listing has been closed!",
        "update": True,
        "isOwner": isOwner,
        "isListingInWatchlist": isListingInWatchlist,
        "allComments": allComments
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
