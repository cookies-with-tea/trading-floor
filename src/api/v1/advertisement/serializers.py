from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

from apps.advertisement.models import Advertisement


class AdvertisementSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=CurrentUserDefault())

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


class AdvertisementListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = [
            'title',
            'type',
            'urgency',
            'author',
        ]
