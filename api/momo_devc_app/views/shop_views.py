from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from ..serializers import ShopSerializer, ScanShopSerializer
from ..models import Shop, Transaction, Profile
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance as D
from django.contrib.gis.db.models.functions import Distance

class ScanInRadius(ListAPIView):
    serializer_class = ScanShopSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        profile = Profile.objects.get(user=user)
        lat = self.request.query_params.get('lat', None)
        long = self.request.query_params.get('long', None)
        lat = float(lat)
        long = float(long)
        rad = self.request.query_params.get('rad', 10)

        point = Point((long, lat), srid=4326)
        shops = Shop.objects.filter(location__distance_lte=(point, D(km=rad))).annotate(
            distance=Distance("location", point)).order_by("distance")
        for shop in shops:
            shop.icon = 'normal'
            num_transaction = Transaction.objects.filter(shop=shop).count()
            if num_transaction > 3:
                shop.icon = 'popular'
            num_transaction = Transaction.objects.filter(user=profile, shop=shop).count()
            if num_transaction > 3:
                shop.icon = 'favorite'
        return shops


class List(ListAPIView):
    serializer_class = ShopSerializer
    permission_classes = [IsAuthenticated]
    queryset = Shop.objects.all()
