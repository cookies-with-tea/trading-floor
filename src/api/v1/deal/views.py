from rest_framework.viewsets import ModelViewSet

from api.v1.deal import serializers
from apps.deal.models import Deal
from apps.user.permissions import IsAuthenticatedAndIsActive


class DealModelViewSet(ModelViewSet):
    serializer_class_map = {
        'retrieve': serializers.DealSerailizer,
        'create': serializers.CreateDealSerializer,
    }
    default_serializer_class = serializers.DealSerailizer

    queryset = Deal.objects.all()
    permission_classes = [IsAuthenticatedAndIsActive]


class FeedBackModelViewSet(ModelViewSet):
    serializer_class_map = {
        'retrieve': serializers.FeedbackSerializer,
        'list': serializers.FeedbakSerializer,
        'create': serializers.CreateFeedbackSerializer,
    }
    default_serializer_class = serializers.FeedbackSerializer

    queryset = Deal.objects.all()
    permission_classes = [IsAuthenticatedAndIsActive]
