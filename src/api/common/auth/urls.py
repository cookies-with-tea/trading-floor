from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from api.common.auth.views import AuthorizationGoogleAPIView, SingUpAPIView

urlpatterns = [
    path('sign-up', SingUpAPIView.as_view(), name='sign-up'),
    path('google', AuthorizationGoogleAPIView.as_view(), name='authorization-google'),
    path('refresh', TokenRefreshView.as_view(), name='refresh-token'),
]
