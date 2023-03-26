from django.urls import path

from api.common.auth.views import SignUpGoogleAPIView

urlpatterns = [
    path('google/', SignUpGoogleAPIView.as_view(), name='sign-up-google'),
]
