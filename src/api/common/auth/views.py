from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.request import Request

from api.common.auth.serializers import GoogleCredentialsSerializer
from apps.user.models import User
from config.settings import GOOGLE_CLIENT_ID
from library.oauth.google import GoogleOauth
from library.oauth.models import GoogleCredentials


class SignUpGoogleAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = GoogleCredentialsSerializer
    permission_classes = [AllowAny]

    def create(self, request: Request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            GoogleOauth.check_google_authentication(
                GoogleCredentials(serializer.data['authorization_code']), google_client_id=GOOGLE_CLIENT_ID
            )

        return AuthenticationFailed(code=403, detail='bad data google')
