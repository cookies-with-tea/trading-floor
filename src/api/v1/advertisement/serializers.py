from rest_framework import serializers

from apps.advertisement.models import Advertisement


class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = [
            'title',
            'description',
            'type',
            'image',
            'urgency',
            'author',
        ]


class ListAdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = [
            'title',
            'type',
            'urgency',
            'author',
        ]
