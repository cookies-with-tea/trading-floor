from django.urls import path

from api.common.auth.views import AuthorizationGoogleAPIView, SingUpAPIView

urlpatterns = [
    path('sign-up', SingUpAPIView.as_view(), name='sign-up'),
    path('google/', AuthorizationGoogleAPIView.as_view(), name='authorization-google'),
]
