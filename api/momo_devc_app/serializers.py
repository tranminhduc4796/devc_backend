from rest_framework import serializers
from .models import User, Merchant, Shop, Item, Category, Transaction


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'embedding']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Item
        fields = '__all__'


class MerchantSerializer(serializers.ModelSerializer):
    menu = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Merchant
        fields = '__all__'


class ShopSerializer(serializers.ModelSerializer):
    merchant = MerchantSerializer(read_only=True)

    class Meta:
        model = Shop
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
        extra_kwargs = {'user': {'required': False}}
