from django.core.management.base import BaseCommand, CommandError
from momo_devc_app.models import Merchant, Item, Category
from django.contrib.gis.geos import Point
import csv


class Command(BaseCommand):
    # def add_arguments(self, parser):
    #     parser.add_argument('shop_id', nargs='+', type=int)

    def handle(self, *args, **options):
        csv_file = './momo_devc_app/management/shop_menu.csv'
        with open(csv_file, 'r') as f:
            f.readline()  # Pass the header
            items_info = csv.reader(f)
            for row in items_info:
                merchant_name = row[1]
                item_name = row[2]
                price = row[3]
                img_url = row[4]
                category_name = row[5]
                category = Category.objects.get_or_create(name=category_name)[0]
                print(merchant_name)
                merchant = Merchant.objects.get(name=merchant_name)
                item = Item.objects.get_or_create(
                    name=item_name,
                    price=price,
                    img_url=img_url,
                    category=category,
                    merchant=merchant
                )


