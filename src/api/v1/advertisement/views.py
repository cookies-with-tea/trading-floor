from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.v1.advertisement.serializers import AdvertisementSerializer
from apps.advertisement.models import Advertisement


class CreateAdvertisementViewSet(viewsets.ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        request.data['author'] = request.user

        return super().create(request)
