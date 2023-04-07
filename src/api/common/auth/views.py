from django.conf import settings
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response

from api.common.auth.serializers import CredentialsModelSerializer, GoogleCredentialsSerializer, SignUpModelSerializer
from apps.user.models import User
from library.oauth.google import GoogleOauth
from library.oauth.models import GoogleCredentials
from utils.strings import is_correct_email_domain


class AuthorizationGoogleAPIView(CreateAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = GoogleCredentialsSerializer
    permission_classes = [AllowAny]

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
        user, is_create = User.objects.get_or_create(email=google_user.email, room_number=0)

        # Сереализуем почту и создаём access и refresh токены
        return Response(CredentialsModelSerializer(user).data, status=status.HTTP_201_CREATED)


class SingUpAPIView(CreateAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = SignUpModelSerializer
    permission_classes = [AllowAny]

    def create(self, request: Request, *args, **kwargs):
        serializer = SignUpModelSerializer(request.user, request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)
