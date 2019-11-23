from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import merchant_views, item_views, shop_views

urlpatterns = [
    path('merchants/', merchant_views.ListCreate.as_view()),
    path('merchants/<int:pk>', merchant_views.RetrieveUpdateDelete.as_view()),
    path('items/<int:merchant>', item_views.List.as_view()),
    path('shops/scan', shop_views.ScanInRadius.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json'])