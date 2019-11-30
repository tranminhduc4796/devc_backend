from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..serializers import MerchantSerializer, ItemSerializer, CategorySerializer
from ..models import Merchant, Category


class ListCreate(ListCreateAPIView):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer
    permission_classes = [IsAuthenticated]


class RetrieveUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer
    permission_classes = [IsAuthenticated]


class ListCategory(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ItemSerializer

    def get(self, request, *args, **kwargs):
        merchant_id = self.kwargs['pk']
        merchant = Merchant.objects.get(pk=merchant_id)
        menu = merchant.menu
        serializer = self.serializer_class(menu, many=True, read_only=True)
        categories = []
        for item in serializer.data:
            category = item['category']
            if category not in categories:
                categories.append(category)
        categories = [Category.objects.get(pk=cate_id) for cate_id in categories]
        cate_serializer = CategorySerializer(categories, many=True, read_only=True)
        return Response(cate_serializer.data)
