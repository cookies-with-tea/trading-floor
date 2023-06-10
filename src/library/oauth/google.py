import oauthlib
from google_auth_oauthlib.flow import Flow

from .models import GoogleCredentials, GoogleUser


class GoogleOauth:
    USER_INFO_URL = 'https://www.googleapis.com/userinfo/v2/me'

    @staticmethod
    def create_flow(secret_file_path: str) -> Flow:
        return Flow.from_client_secrets_file(secret_file_path, scopes=None, redirect_uri='postmessage')

    @classmethod
    def google_authentication(cls, user: GoogleCredentials, flow: Flow) -> GoogleUser | None:
        try:
            flow.fetch_token(code=user.authorization_code)
        except oauthlib.oauth2.rfc6749.errors.InvalidGrantError:
            return None

        google_user: dict = flow.authorized_session().get(cls.USER_INFO_URL, verify=False).json()

        return GoogleUser(email=google_user['email'], picture=google_user['picture'])
