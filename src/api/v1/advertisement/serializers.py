from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

from apps.advertisement.models import Advertisement, AdvertisementCategory, Image


class ImageSerializer(serializers.ModelSerializer):
    url = serializers.FileField(source='image')

    class Meta:
        model = Image
        fields = [
            'url',
        ]


class CreateAdvertisementSerializer(serializers.ModelSerializer):
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
            'category',
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

    def to_representation(self, instance) -> dict:
        return AdvertisementSerializer(instance).data


class AdvertisementCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvertisementCategory
        fields = ['id', 'title']


class AdvertisementSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=CurrentUserDefault())
    images = ImageSerializer(many=True)
    category = AdvertisementCategorySerializer(read_only=True)

    class Meta:
        model = Advertisement
        fields = [
            'title',
            'description',
            'advertisement_type',
            'images',
            'urgency_type',
            'author',
            'category',
        ]


class AdvertisementListSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=CurrentUserDefault())
    category = AdvertisementCategorySerializer()

    class Meta:
        model = Advertisement
        fields = [
            'title',
            'advertisement_type',
            'urgency_type',
            'author',
            'category',
        ]
