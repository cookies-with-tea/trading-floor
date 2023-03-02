from rest_framework.generics import RetrieveUpdateDestroyAPIView

from .models import User
from .permissions import IsOwnerProfileOrReadOnly
from .serializer import UserProfileSerializer


class UserProfileAPIUpdate(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsOwnerProfileOrReadOnly]
