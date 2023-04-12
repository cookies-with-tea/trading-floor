from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from apps.user.models import User


class GoogleCredentialsSerializer(serializers.Serializer):
    authorization_code = serializers.CharField()


class CredentialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['is_register']
        read_only_fields = ['access', 'refresh', 'is_register']

    def to_representation(self, instance: User):
        data = super().to_representation(instance)

        refresh: RefreshToken = RefreshToken.for_user(instance)

        data.update(refresh=str(refresh))
        data.update(access=str(refresh.access_token))

        return data


class SignUpSerializer(serializers.ModelSerializer):
    is_register = serializers.HiddenField(default=True)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'room_number',
            'avatar',
            'is_register',
        ]
