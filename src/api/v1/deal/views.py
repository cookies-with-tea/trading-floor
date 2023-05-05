from rest_framework.viewsets import ModelViewSet

from api.v1.deal import serializers
from apps.deal.models import Deal
from apps.user.permissions import IsAuthenticatedAndIsActive
from utils.mixins.views import SerializerClassMapMixin


class DealModelViewSet(SerializerClassMapMixin, ModelViewSet):
    serializer_class_map = {
        'retrieve': serializers.DealSerailizer,
        'create': serializers.CreateDealSerializer,
    }
    default_serializer_class = serializers.DealSerailizer

    queryset = Deal.objects.filter(is_response=False)
    permission_classes = [IsAuthenticatedAndIsActive]


class FeedBackModelViewSet(SerializerClassMapMixin, ModelViewSet):
    serializer_class_map = {
        'retrieve': serializers.FeedbackSerializer,
        'list': serializers.FeedbackSerializer,
        'create': serializers.CreateFeedbackSerializer,
    }
    default_serializer_class = serializers.FeedbackSerializer

    queryset = Deal.objects.filter(is_response=True)
    permission_classes = [IsAuthenticatedAndIsActive]
