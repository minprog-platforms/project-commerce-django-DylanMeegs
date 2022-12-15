# MeegsBay

Website that allows users to create listings. Others can then view those listings, bid on them, add the listings to a watchlist, and even leave comments on the listings.

## Getting started

To get started with this website, you must download the code from this repository, and run "python3 manage.py runserver" in the terminal. If you want to start your own database, you need to create a superuser with the following command in the terminal "python3 manage.py createsuperuser". Once that is done, you can go to the admin and create categories, so you can start creating listings (The site does not come with categories if you do not have a database containing the categories and the site will produce errors if you create a listing without a category.)


## Workflow

The text below displays the general workflow of MeegsBay:
The default page is the active listings page. On this page you can see all the active listings if there are any. On this page there is also a dropdown menu for filtering the active listings on category. The listings themselves show the image of the listing, if any, the title, description, current price, a details button which links to the listing page, and the category it is in.

The header of the website changes whether the user is logged in or not.

When the user **is not** logged in, the user has the option to register, to log in or to view the active listings. On the active listings page, the user can also access the individual listings. However, some parts of the individual listing page are not visible when a user is not logged in. Parts such as the bidding option, commenting option and the option to add the listing to the watchlist are not yet present.

When the user **is** logged in, the header changes. The user is now also able to create a new listing, and view their watchlist.

Creating a listing goes as follows: You click on "Create New Listing" in the navbar. You enter a title, description, imageURL, price, and category for the listing and then the listing is stored in the database.

Viewing your watchlist goed as follows: You click on "Watchlist" in the navbar, and there you see every listing you have added to the watchlist, even if the listing has been closed.

When you are on a listing page you see the title, image, description, owner of the listing, current price, and the comments.

However, that is not all. On top of this, if the user is signed in they can also access parts of the website that were previously locked. Such as:
- An "add listings to watchlist" button
- Bid on active listings
- Comment on active listings

Lastly, the "Log in" button changed to "Log out" and the user is immediately logged out, and returned to the main page upon clicking this button.

When the logged in user is on an individual listings page of their own, then there is also a button which enables the user to close the auction. The user that has won the auction is able to view that they won the bidding when they enter the url of the closed bidding.

### Class Diagram

There will be five main models for this website:

- The User class - This contains the information of the user if they're logged in, namely username, e-mailaddress and password.

- The Category class - This will contain a name for the categories on the website, these are the same categories as on eBay.

- The Bid class - This contains all the information of a bid on a listing. It contains the amount of the bid, who placed it, and on which listing.

- The Comment class - This contains all the information of the comments on a listing. It contains the message of the comment, the user who placed it, and on which listing.

- The Listing class - This contains all the information of a listing, namely the title of the listing, the description of the listing, the image of the listing, the price it has, if the listing is active, who is the owner, which category is it in and if it is on the watchlist of the user that is viewing the listing.

![Overview](images/ClassDiagram.png)

### Databases per page

#### Active listings

This page will use the listing, and Category model.

#### Create listing

This page will use the listing model.

#### Listing page

This page will use the listing, bid, and comment models.

#### Watchlist

This page will use the Listings model.
