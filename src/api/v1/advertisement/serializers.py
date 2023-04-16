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


class AdvertisementCreateSerializer(serializers.ModelSerializer):
    PERMISSIBLE_ADVERTISEMENT_TYPES = (
        ('EXCHANGE'),
        ('SELL'),
        ('BUY'),
        ('GIVE'),
        ('TAKE'),
        ('EXCHANGE', 'SELL'),
        ('EXCHANGE', 'BUY'),
        ('EXCHANGE', 'GIVE'),
        ('EXCHANGE', 'TAKE'),
        ('SELL', 'GIVE'),
        ('BUY', 'TAKE'),
        ('EXCHANGE', 'SELL', 'GIVE'),
        ('EXCHANGE', 'BUY', 'TAKE'),
    )

    author = serializers.HiddenField(default=CurrentUserDefault())
    images = ImageSerializer(many=True)

    def validate_type(self, value):
        if value not in self.PERMISSIBLE_ADVERTISEMENT_TYPES:
            raise TypeError('Некорректный тип объявления')
        return value

    class Meta:
        model = Advertisement
        fields = [
            'title',
            'description',
            'advertisement_type',
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
            'advertisement_type',
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
            'advertisement_type',
            'urgency_type',
            'author',
        ]
