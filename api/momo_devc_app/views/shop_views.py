from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from ..serializers import ShopSerializer
from ..models import Shop
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance


class ScanInRadius(ListAPIView):
    serializer_class = ShopSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        lat = self.request.query_params.get('lat', None)
        long = self.request.query_params.get('long', None)
        lat = float(lat)
        long = float(long)
        rad = self.request.query_params.get('rad', 10)

        point = Point((long, lat), srid=4326)
        shops = Shop.objects.filter(location__distance_lte=(point, Distance(km=rad)))
        return shops


class List(ListAPIView):
    serializer_class = ShopSerializer
    permission_classes = [IsAuthenticated]
    queryset = Shop.objects.all()
