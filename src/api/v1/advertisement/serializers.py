from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

from apps.advertisement.models import Advertisement, Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = [
            'title',
            'advertisement',
        ]


class AdvertisementSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=CurrentUserDefault())
    images = ImageSerializer(many=True)

    class Meta:
        model = Advertisement
        fields = [
            'title',
            'description',
            'type',
            'images',
            'urgency_type',
            'author',
        ]


class AdvertisementListSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Advertisement
        fields = [
            'title',
            'type',
            'urgency_type',
            'author',
        ]
