from django.contrib import admin
from .models import Profile, Merchant, Shop, Item, Transaction, Category

admin.site.register(Profile)
admin.site.register(Merchant)
admin.site.register(Shop)
admin.site.register(Item)
admin.site.register(Transaction)
admin.site.register(Category)
