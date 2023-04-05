from rest_framework.viewsets import ModelViewSet

from api.v1.advertisement import serializers
from apps.advertisement.models import Advertisement
from apps.user.permissions import IsAuthenticatedAndIsActive
from utils.mixins.views import SerializerClassMapMixin


class AdvertisementModelViewSet(SerializerClassMapMixin, ModelViewSet):
    serializer_class_map = {
        'create': serializers.AdvertisementSerializer,
        'retrieve': serializers.AdvertisementSerializer,
        'list': serializers.AdvertisementListSerializer,
    }
    default_serializer_class = serializers.AdvertisementSerializer

    queryset = Advertisement.objects.all()
    permission_classes = [IsAuthenticatedAndIsActive]
