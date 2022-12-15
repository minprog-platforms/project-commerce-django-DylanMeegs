from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    categoryName = models.CharField(max_length=50)

    def __str__(self):
        return self.categoryName

class Bid(models.Model):
    bid = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userBid", null=True, blank=True)

class Listing(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    imageurl = models.CharField(max_length=800)
    price = models.ForeignKey(Bid, on_delete=models.CASCADE, blank=True, null=True, related_name="bidPrice")
    is_active = models.BooleanField(default=True, blank=False, null=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user", null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category", null=True, blank=True)
    watchlist = models.ManyToManyField(User, blank=True, null=True, related_name="listingWatchlist")

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userComment", null=True, blank=True)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="listingComment", null=True, blank=True)
    message = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.author} comment on {self.listing}"
