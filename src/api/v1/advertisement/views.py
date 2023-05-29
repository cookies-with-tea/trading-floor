from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from api.v1.advertisement import serializers, utils
from api.v1.advertisement.filters import AdvertisementFilter
from api.v1.advertisement.serializers import AdvertisementCategorySerializer
from apps.advertisement.models import Advertisement, AdvertisementCategory
from apps.user.permissions import IsAuthenticatedAndIsActive
from utils.mixins.views import SerializerClassMapMixin


class AdvertisementModelViewSet(SerializerClassMapMixin, ModelViewSet):
    serializer_class_map = {
        'create': serializers.CreateAdvertisementSerializer,
        'retrieve': serializers.AdvertisementSerializer,
        'list': serializers.AdvertisementListSerializer,
    }
    default_serializer_class = serializers.AdvertisementSerializer

    queryset = Advertisement.objects.all()
    pagination_class = utils.StandardResultsSetPagination
    permission_classes = [IsAuthenticatedAndIsActive]
    filterset_class = AdvertisementFilter


class AdvertisementCategoryListAPIView(ListAPIView):
    serializer_class = AdvertisementCategorySerializer
    permission_classes = [IsAuthenticatedAndIsActive]
    queryset = AdvertisementCategory.objects.all()
