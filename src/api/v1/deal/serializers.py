from rest_framework import serializers

from api.v1.user.serializers import UserProfileSerializer
from apps.deal.models import Deal


class DealSerailizer(serializers.Serializer):
    seller = UserProfileSerializer()
    buyer = UserProfileSerializer()

    class Meta:
        model = Deal
        fields = [
            'advertisement',
            'seller',
            'buyer',
            'status',
            'created_at',
        ]


class CreateFeedbackSerializer(serializers.Serializer):
    class Meta:
        model = Deal
        fields = [
            'advertisement',
            'seller',
            'buyer',
        ]


class FeedbackListSerializer(serializers.Serializer):
    seller = UserProfileSerializer()
    buyer = UserProfileSerializer()

    class Meta:
        model = Deal
        fields = [
            'id',
            'advertisement',
            'seller',
            'buyer',
            'created_at',
            'is_response',
        ]
