from rest_framework import serializers

from apps.user.models import User


class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = User
        fields = [
            'email',
            'first_name',
            'last_name',
            'room_number',
            'avatar',
            'created_at',
            'updated_at',
            'is_active',
            'is_admin',
        ]
