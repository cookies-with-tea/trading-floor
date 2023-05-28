from django.urls import path
from rest_framework import routers

from api.v1.advertisement.views import AdvertisementCategoryListAPIView, AdvertisementModelViewSet

router = routers.SimpleRouter()
router.register('', AdvertisementModelViewSet, basename='advertisements')

urlpatterns = [
    path('categories', AdvertisementCategoryListAPIView.as_view(), name='categories-list'),
] + router.urls
