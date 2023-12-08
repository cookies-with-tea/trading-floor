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


class CreateDealSerializer(serializers.ModelSerializer):
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

    def update(self, instance: Deal, validated_data: dict) -> Deal:
        instance.is_response = False
        instance.status = Deal.STATUS_OPEN
        instance.save()

        return instance


class CreateFeedbackSerializer(serializers.ModelSerializer):
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
