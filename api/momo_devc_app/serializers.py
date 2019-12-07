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

    class Meta:
        model = Transaction
        fields = '__all__'
        extra_kwargs = {'user': {'required': False}}

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        items = [Item.objects.get(pk=i) for i in ret['item']]
        shop = Shop.objects.get(pk=ret['shop'])
        item_serializer = ItemSerializer(items, many=True, read_only=True)
        shop_serializer = ShopSerializer(shop, read_only=True)
        ret['item'] = item_serializer.data
        ret['shop'] = shop_serializer.data
        return ret
