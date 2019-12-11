from django.core.management.base import BaseCommand, CommandError
from momo_devc_app.models import Shop, Merchant
from django.contrib.gis.geos import Point
import csv


class Command(BaseCommand):
    # def add_arguments(self, parser):
    #     parser.add_argument('shop_id', nargs='+', type=int)

    def handle(self, *args, **options):
        csv_file = './momo_devc_app/management/truy_vet_item.csv'
        with open(csv_file, 'r') as f:
            f.readline()  # Pass the header
            shops_info = csv.reader(f)
            for row in shops_info:
                shop_name = row[1]
                merchant_name = row[2]
                shop_long = float(row[3])
                shop_lat = float(row[4])
                shop_add = row[5]
                point = Point((shop_long, shop_lat), srid=4326)
                merchant = Merchant.objects.get_or_create(name=merchant_name)[0]
                shop = Shop.objects.get_or_create(
                    address=shop_add,
                    location=point,
                    merchant=merchant
                )
                print('Imported', shop)
