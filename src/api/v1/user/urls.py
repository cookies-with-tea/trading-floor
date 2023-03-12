from django.urls import path

from .views import MeAPIView, SignUpAPIView, UserProfileAPIView

urlpatterns = [
    path('<int:pk>', UserProfileAPIView.as_view(), name='user-detail'),
    path('me', MeAPIView.as_view(), name='user-me'),
    path('', SignUpAPIView.as_view(), name='sign-up'),
]
