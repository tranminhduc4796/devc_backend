from django.contrib import admin
from .models import User, Merchant, Shop, Item, Transaction, Category

admin.site.register(User)
admin.site.register(Merchant)
admin.site.register(Shop)
admin.site.register(Item)
admin.site.register(Transaction)
admin.site.register(Category)
