from rest_framework.generics import CreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from api.v1.user.serializers import UserProfileSerializer
from apps.user.models import User


class SignUpAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [AllowAny]


class MeAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]


class UserProfileAPIView(RetrieveAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
