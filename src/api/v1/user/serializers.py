from django.core.files.storage import default_storage
from rest_framework import serializers

from apps.user.models import User
from utils.colors import generate_random_color


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
            'telegram_username',
            'vk_username',
            'room_number',
            'avatar',
            'avatar_color',
            'created_at',
            'updated_at',
            'is_active',
            'is_staff',
        ]


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'telegram_username',
            'vk_username',
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
        fields = ['avatar', 'first_name', 'last_name', 'telegram_username', 'vk_username']

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
