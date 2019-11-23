from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from ..serializers import MerchantSerializer, ItemSerializer
from ..models import Merchant, Item


class List(ListAPIView):
    serializer_class = MerchantSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        merchant_id = self.kwargs['merchant']
        merchant = Merchant.objects.filter(pk=merchant_id)
        return merchant

