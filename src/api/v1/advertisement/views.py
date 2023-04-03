from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.v1.advertisement import serializers
from apps.advertisement.models import Advertisement


class AdvertisementModelViewSet(viewsets.ModelViewSet):
    serializer_classes = {
        'create': serializers.AdvertisementSerializer,
        'retrieve': serializers.AdvertisementSerializer,
        'list': serializers.AdvertisementListSerializer,
    }

    default_serializer_class = serializers.AdvertisementSerializer
    queryset = Advertisement.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)
