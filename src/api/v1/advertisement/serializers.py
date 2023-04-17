from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

from apps.advertisement.models import Advertisement, Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = [
            'image',
            'advertisement',
        ]


class AdvertisementCreateSerializer(serializers.ModelSerializer):
    PERMISSIBLE_ADVERTISEMENT_TYPES = (
        ('Обмен'),
        ('Продам'),
        ('Куплю'),
        ('Отдам'),
        ('Возьму'),
        ('Обмен', 'Продам'),
        ('Обмен', 'Куплю'),
        ('Обмен', 'Отдам'),
        ('Обмен', 'Возьму'),
        ('Продам', 'Отдам'),
        ('Куплю', 'Возьму'),
        ('Обмен', 'Продам', 'Отдам'),
        ('Обмен', 'Куплю', 'Возьму'),
    )

    author = serializers.HiddenField(default=CurrentUserDefault())
    images = serializers.ListField(
        child=serializers.ImageField(
            allow_empty_file=False,
            use_url=False,
        ),
        write_only=True,
    )

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

    def validate_type(self, value):
        if value not in self.PERMISSIBLE_ADVERTISEMENT_TYPES:
            raise TypeError('Некорректный тип объявления')
        return value

    def create(self, validated_data: dict) -> Meta.model:
        uploaded_images = validated_data.pop('images')
        advertisement = Advertisement.objects.create(**validated_data)
        for image in uploaded_images:
            Image.objects.create(
                advertisement=advertisement,
                image=image,
            )

        return advertisement


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
