from django.db import models


'''
Relationships between models:

-: One to One,
-<: One to Many,
><: Many to Many

User -< Transactions
Merchant -< Shop
Merchant -< Item
Item >< Transactions
Item >< Category
'''


class User(models.Model):
    username = models.CharField(max_length=50)
    pwd = models.CharField(min_length=8, max_length=16)
    email = models.EmailField()


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Merchant(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Shop(models.Model):
    address = models.CharField(max_length=50)
    # Many to one with Merchant. With a Merchant instance, list of shops can be gotten by Merchant.shops.all()
    brand = models.ForeignKey(
        Merchant, on_delete=models.CASCADE, blank=False, related_name="shops")

    def __str__(self):
        return str(self.brand) + ": " + self.address


class Item(models.Model):
    name = models.TextField()
    price = models.FloatField()
    # Many to many with Category. With a Category instance, list of items can be gotten by Category.items.all()
    categories = models.ManyToManyField(Category, related_name='items')
    # Many to one with Merchant. With a Merchant instance, list of items can be gotten by Merchant.menu.all()
    brand = models.ForeignKey(
        Merchant, on_delete=models.CASCADE, blank=False, related_name="menu")

    def __str__(self):
        return self.name + ' - ' + str(self.brand) + ' - ' + str(self.price)


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    datetime = models.DateTimeField(auto_now_add=True)
    # Many to one with Shop
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, blank=False)
    # Many to many with Item
    item = models.ManyToManyField(
        Item, blank=False, related_name='transactions')

    def __str__(self):
        return str(self.datetime) + ', ' + str(self.user) + ' bought ' + str(self.item) + ' at ' + str(self.shop)
