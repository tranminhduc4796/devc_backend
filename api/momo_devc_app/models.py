from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User


'''
Relationships between models:

-: One to One,
-<: One to Many,
><: Many to Many

User -< Transactions
Brands -< Shops
Brands -< Items
Item >< Transactions
Item >< Categories
'''


class Categories(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name


class Brands(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name


class Shops(models.Model):
    address = models.CharField()
    # Many to one with Brands. With a Brand instance, list of shops can be gotten by Brand.shops.all()
    brand = models.ForeignKey(
        Brands, on_delete=models.CASCADE, blank=False, related_name="shops")

    def __str__(self):
        return self.brand + ": " + self.address


class Items(models.Model):
    name = models.TextField()
    price = models.FloatField()
    # Many to many with Categories. With a Categories instance, list of items can be gotten by Categories.items.all()
    categories = models.ManyToManyField(Categories, related_name='items')
    # Many to one with Brands. With a Brand instance, list of items can be gotten by Brand.menu.all()
    brand = models.ForeignKey(
        Brands, on_delete=models.CASCADE, blank=False, related_name="menu")

    def __str__(self):
        return self.name + ' - ' + self.categories + ' - ' + self.price


class Transactions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    datetime = models.DateTimeField(auto_now_add=True)
    # Many to one with Shops
    shop = models.ForeignKey(Shops, on_delete=models.CASCADE, blank=False)
    # Many to many with Items
    item = models.ManyToManyField(
        Items, blank=False, related_name='transactions')

    def __str__(self):
        return self.datetime + ', ' + self.user + ' bought ' + self.item + ' at ' + self.shop
