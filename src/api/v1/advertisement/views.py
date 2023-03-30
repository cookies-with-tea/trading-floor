from rest_framework import viewsets
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from api.v1.advertisement.serializers import AdvertisementSerializer, ListAdvertisementSerializer
from apps.advertisement.models import Advertisement


class CreateAdvertisementViewSet(viewsets.ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        request.data['author'] = request.user

        return super().create(request)


class RetrieveAdvertisementAPIView(RetrieveAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsAuthenticated]


class ListAdvertisementAPIView(ListAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = ListAdvertisementSerializer
    permission_classes = [IsAuthenticated]
