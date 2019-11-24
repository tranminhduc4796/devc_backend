from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from ..serializers import ItemSerializer
from ..models import Merchant, Item


class List(ListAPIView):
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        merchant_id = self.kwargs['merchant']
        category_id = self.request.query_params.get('category', None)
        items = Item.objects.filter(merchant=merchant_id)
        if category_id is not None:
            items = items.filter(category=category_id)
        return items


