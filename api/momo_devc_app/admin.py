from django.contrib import admin
from .models import Brands, Shops, Items, Transactions

admin.site.register(Brands)
admin.site.register(Shops)
admin.site.register(Items)
admin.site.register(Transactions)
