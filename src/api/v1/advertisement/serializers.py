from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

from apps.advertisement.models import Advertisement, Image
from utils.strings import PERMISSIBLE_ADVERTISEMENT_TYPE


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = [
            'title',
            'advertisement',
        ]


class AdvertisementCreateSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=CurrentUserDefault())
    images = ImageSerializer(many=True)

    def validate_type(self, value):
        if value not in PERMISSIBLE_ADVERTISEMENT_TYPE:
            raise TypeError('Некорректный тип объявления')
        return value

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
