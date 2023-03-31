from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.v1.advertisement.serializers import AdvertisementSerializer
from apps.advertisement.models import Advertisement


class AdvertisementModelViewSet(viewsets.ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        request.data._mutable = True
        request.data['author'] = request.user.id
        request.data._mutable = False

        return super().create(request)
