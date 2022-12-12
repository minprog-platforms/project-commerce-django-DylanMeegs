from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    categoryName = models.CharField(max_length=50)

    def __str__(self):
        return self.categoryName

class Listing(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    imageurl = models.CharField(max_length=800)
    price = models.FloatField()
    is_active = models.BooleanField(default=True, blank=False, null=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user", null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category", null=True, blank=True)

    def __str__(self):
        return self.title
