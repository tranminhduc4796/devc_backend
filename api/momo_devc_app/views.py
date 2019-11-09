from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MerchantSerializer, ShopSerializer, ItemSerializer, CategorySerializer, TransactionSerializer


@api_view(['POST'])
def recommend_products(request):
    # Recommend products when a user make a transaction.
    if request.method == 'POST':
        data = request.data
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status = status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(data, status = status.HTTP_201_CREATED)
