from rest_framework import status
from rest_framework.generics import RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.v1.user.serializers import UpdateUserSerializer, UserDetailSerializer, UserProfileSerializer
from apps.user.models import User
from utils.mixins.views import SerializerClassMapHttpMethodMixin


class MeAPIView(SerializerClassMapHttpMethodMixin, RetrieveUpdateDestroyAPIView):
    queryset = User.objects.filter(is_active=True)
    permission_classes = [IsAuthenticated]

    default_serializer_class = UserDetailSerializer
    serializer_class_map = {
        'PUT': UpdateUserSerializer,
        'PATCH': UpdateUserSerializer,
        'GET': UserDetailSerializer,
    }

    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()(request.user, context={'request': request})

        return Response(serializer.data)

    def get_object(self):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        request.user.is_active = False
        request.user.save()

        return Response(status=status.HTTP_204_NO_CONTENT)


class UserProfileAPIView(RetrieveAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
