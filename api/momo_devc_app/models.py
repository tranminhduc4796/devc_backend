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
    brand = models.ForeignKey(
        Brands, on_delete=models.CASCADE, blank=False, related_name="shops")


class Items(models.Model):
    name = models.TextField()
    categories = ArrayField(models.CharField())
    brand = models.ForeignKey(
        Brands, on_delete=models.CASCADE, blank=False, related_name="menu")


class Transactions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    shop = models.ForeignKey(Shops, on_delete=models.CASCADE, blank=False)
    item = models.ManyToManyField(Items, blank=False)
