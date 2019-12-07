from rest_framework import serializers
from .models import Profile, Merchant, Shop, Item, Category, Transaction
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ['user', 'embedding']


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
    coordinate = serializers.SerializerMethodField('get_xy')

    def get_xy(self, shop):
        return shop.location.coords

    class Meta:
        model = Shop
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    item = ItemSerializer(read_only=True, many=True)
    shop = ShopSerializer(read_only=True, many=True)

    class Meta:
        model = Transaction
        fields = '__all__'
        extra_kwargs = {'user': {'required': False}}
