from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from api.v1.advertisement.serializers import AdvertisementSerializer
from apps.advertisement.models import Advertisement


class CreateAdvertisementAPIView(CreateAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsAuthenticated]
