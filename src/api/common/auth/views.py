import uuid

import requests
from django.conf import settings
from django.core.files.base import ContentFile
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response

from api.common.auth.serializers import CredentialsSerializer, GoogleCredentialsSerializer, SignUpSerializer
from apps.user.models import User
from library.oauth.google import GoogleOauth
from library.oauth.models import GoogleCredentials
from utils.strings import is_correct_email_domain


class AuthorizationGoogleAPIView(CreateAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = GoogleCredentialsSerializer
    permission_classes = [AllowAny]

    @extend_schema(responses=CredentialsSerializer)
    def create(self, request: Request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            return AuthenticationFailed(code=403, detail='bad data google')

        # Получаем данные пользователя по id_token из Google
        flow = GoogleOauth.create_flow(settings.ROOT_GOOGLE_SECRET_CLIENTS_FILE)

        google_user = GoogleOauth.google_authentication(
            user=GoogleCredentials(serializer.data['authorization_code']),
            flow=flow,
        )

        # Валидируем данные, которые приходят
        if not is_correct_email_domain(google_user.email, settings.EMAIL_DOMAIN):
            return Response(
                {'email': [f'Разрешены только адреса домена {settings.EMAIL_DOMAIN}']},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Cоздаём или получаем пользователя
        user, is_create = User.objects.get_or_create(
            email=google_user.email, defaults={'is_register': False, 'room_number': 0}
        )

        if is_create:
            # Получаем содержимое фотографии по ссылке
            response = requests.get(google_user.picture)

            # Генерируем рандомное имя файла
            file_name = str(uuid.uuid4())

            user.avatar.save(file_name, ContentFile(response.content), save=True)

        # Сереализуем почту и создаём access и refresh токены
        return Response(CredentialsSerializer(user).data, status=status.HTTP_201_CREATED)


class SingUpAPIView(CreateAPIView):
    queryset = User.objects.filter(is_register=False)
    serializer_class = SignUpSerializer
    permission_classes = [AllowAny]

    @extend_schema(responses=CredentialsSerializer)
    def create(self, request: Request, *args, **kwargs):
        serializer = SignUpSerializer(request.user, request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(CredentialsSerializer(request.user).data, status=status.HTTP_200_OK)
