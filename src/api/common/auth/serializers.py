from rest_framework import serializers


class GoogleCredentialsSerializer(serializers.Serializer):
    authorization_code = serializers.CharField()
