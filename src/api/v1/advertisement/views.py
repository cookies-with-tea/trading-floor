from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from api.v1.advertisement import serializers
from api.v1.advertisement.filters import AdvertisementFilter
from api.v1.advertisement.serializers import AdvertisementCategorySerializer
from apps.advertisement.models import Advertisement, AdvertisementCategory
from utils.mixins.views import SerializerClassMapMixin


class AdvertisementListPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 20


class AdvertisementModelViewSet(SerializerClassMapMixin, ModelViewSet):
    serializer_class_map = {
        'create': serializers.CreateAdvertisementSerializer,
        'retrieve': serializers.AdvertisementSerializer,
        'list': serializers.AdvertisementListSerializer,
    }
    default_serializer_class = serializers.AdvertisementSerializer

    queryset = Advertisement.objects.all().order_by('-created_at')
    filterset_class = AdvertisementFilter
    pagination_class = AdvertisementListPagination


class AdvertisementCategoryListAPIView(ListAPIView):
    serializer_class = AdvertisementCategorySerializer
    queryset = AdvertisementCategory.objects.all()
