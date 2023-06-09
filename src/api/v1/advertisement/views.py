from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from api.v1.advertisement import serializers
from api.v1.advertisement.filters import AdvertisementFilter
from api.v1.advertisement.serializers import AdvertisementCategorySerializer
from apps.advertisement.models import Advertisement, AdvertisementCategory
from utils.mixins.views import SerializerClassMapMixin


class AdvertisementModelViewSet(SerializerClassMapMixin, ModelViewSet):
    serializer_class_map = {
        'create': serializers.CreateAdvertisementSerializer,
        'retrieve': serializers.AdvertisementSerializer,
        'list': serializers.AdvertisementListSerializer,
    }
    default_serializer_class = serializers.AdvertisementSerializer

    queryset = Advertisement.objects.all()
    filterset_class = AdvertisementFilter


class AdvertisementCategoryListAPIView(ListAPIView):
    serializer_class = AdvertisementCategorySerializer
    queryset = AdvertisementCategory.objects.all()
