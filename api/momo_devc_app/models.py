from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.db import models as geo_models

'''
Relationships between models:

-: One to One,
-<: One to Many,
><: Many to Many

User -< Transactions
Merchant -< Shop
Merchant -< Item
Item >< Transactions
Item -< Category
'''


class Profile(User):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile", parent_link=True)
    embedding = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Merchant(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Shop(models.Model):
    location = geo_models.PointField(unique=True, blank=False, null=False)
    address = models.CharField(max_length=150)
    # Many to one with Merchant. With a Merchant instance, list of shops can be gotten by Merchant.shops.all()
    merchant = models.ForeignKey(
        Merchant, on_delete=models.CASCADE, blank=False, related_name="shops")

    class Meta:
        ordering = ['location']

    def __str__(self):
        return str(self.merchant) + ": " + str(self.address) + ": " + str(self.location)


class Item(models.Model):
    name = models.CharField(max_length=150)
    price = models.FloatField()
    embedding = models.TextField()
    # Many to one with Category. With a Category instance, list of items can be gotten by Category.items.all()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    # Many to one with Merchant. With a Merchant instance, list of items can be gotten by Merchant.menu.all()
    merchant = models.ForeignKey(
        Merchant, on_delete=models.CASCADE, blank=False, related_name="menu")

    class Meta:
        ordering = ['category']

    def __str__(self):
        return str(self.name) + ' - ' + str(self.merchant) + ' - ' + str(self.price)


class Transaction(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    # Many to one with Shop
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, blank=False)
    # Many to many with Item
    item = models.ManyToManyField(
        Item, blank=False, related_name='transactions')
    solved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created']
