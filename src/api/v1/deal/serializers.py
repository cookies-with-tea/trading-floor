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


class CreateDealSerializer(serializers.Serializer):
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
            'is_response',
        ]

    def create(self, validated_data: dict) -> Meta.model:
        validated_data['is_response'] = True
        validated_data['status'] = Deal.STATUS_OPEN
        deal = Deal.objects.create(**validated_data)

        return deal


class CreateFeedbackSerializer(serializers.Serializer):
    class Meta:
        model = Deal
        fields = [
            'advertisement',
            'seller',
            'buyer',
        ]


class FeedbackSerializer(serializers.Serializer):
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
