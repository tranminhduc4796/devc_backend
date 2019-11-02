from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User


'''
Relationships between models:

-: One to One,
-<: One to Many,
><: Many to Many

User -< Transactions
Brands -< Shops, Items
Item >< Tractions
'''


class Brands(models.Model):
    name = models.CharField()


class Shops(models.Model):
    address = models.CharField()
    # Many to one with Brands. With a Brand instance, list of shops can be gotten by Brand.shops.all()
    brand = models.ForeignKey(
        Brands, on_delete=models.CASCADE, blank=False, related_name="shops")


class Items(models.Model):
    name = models.TextField()
    categories = ArrayField(models.CharField())
    # Many to one with Brands. With a Brand instance, list of items can be gotten by Brand.menu.all()
    brand = models.ForeignKey(
        Brands, on_delete=models.CASCADE, blank=False, related_name="menu")


class Transactions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    # Many to one with Shops
    shop = models.ForeignKey(Shops, on_delete=models.CASCADE, blank=False)
    # Many to many with Items
    item = models.ManyToManyField(Items, blank=False)
