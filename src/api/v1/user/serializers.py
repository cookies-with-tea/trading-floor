from django.core.files.storage import default_storage
from rest_framework import serializers
from rest_framework.utils.serializer_helpers import ReturnDict

from apps.advertisement.models import Advertisement
from apps.user.models import User
from utils.colors import generate_random_color


class UserDetailSerializer(serializers.ModelSerializer):
    open_advertisements = serializers.SerializerMethodField()
    closed_advertisements = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'first_name',
            'room_number',
            'avatar',
            'avatar_color',
            'created_at',
            'updated_at',
            'is_active',
            'is_staff',
            'open_advertisements',
            'closed_advertisements',
        ]

    """
    def get_open_advertisements(self, instance: User) -> ReturnDict:
        from api.v1.advertisement.serializers import AdvertisementByUserSerializer

        return AdvertisementByUserSerializer(
            Advertisement.objects.filter(author=instance, is_open=True), many=True
        ).data

    def get_closed_advertisements(self, instance: User) -> ReturnDict:
        from api.v1.advertisement.serializers import AdvertisementByUserSerializer

        return AdvertisementByUserSerializer(
            Advertisement.objects.filter(author=instance, is_open=False), many=True
        ).data
    """


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'room_number',
            'avatar',
            'avatar_color',
            'created_at',
            'updated_at',
            'is_active',
            'is_staff',
        ]


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['avatar', 'first_name', 'last_name']

    def to_representation(self, instance):
        return UserDetailSerializer(instance).data

    def update(self, instance: User, validated_data: dict) -> User:
        avatar = validated_data.pop('avatar', None)
        instance = super().update(instance, validated_data)

        if avatar:
            self._process_avatar(instance, avatar)
        else:
            self._generate_avatar_color(instance)

        instance.save()

        return instance

    def _process_avatar(self, instance, avatar):
        if instance.avatar:
            default_storage.delete(instance.avatar.name)
        instance.avatar.save(avatar.name, avatar)
        instance.avatar_color = None

    def _generate_avatar_color(self, instance):
        instance.avatar_color = generate_random_color()
