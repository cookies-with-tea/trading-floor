from google.auth.transport import requests
from google.oauth2 import id_token

from .models import GoogleCredentials


class GoogleOauth:
    @staticmethod
    def check_google_authentication(user: GoogleCredentials, google_client_id: str) -> bool:
        user_data: dict = id_token.verify_oauth2_token(user.token, requests.Request(), google_client_id)

        print(user_data)

        return True
