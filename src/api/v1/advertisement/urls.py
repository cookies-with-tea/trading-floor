from django.urls import path
from rest_framework import routers

from api.v1.advertisement.views import (
    CreateAdvertisementViewSet,
    ListAdvertisementAPIView,
    RetrieveAdvertisementAPIView,
)

router = routers.SimpleRouter()
router.register('advertisements', CreateAdvertisementViewSet)

urlpatterns = [
    path('<int:pk>', RetrieveAdvertisementAPIView.as_view(), name='advertisement-detail'),
    path('list', ListAdvertisementAPIView.as_view(), name='all-advertisement'),
] + router.urls
