from django.urls import path

from api.v1.user.views import MeAPIView, UserProfileAPIView

urlpatterns = [
    path('<int:pk>', UserProfileAPIView.as_view(), name='user-detail'),
    path('me', MeAPIView.as_view(), name='user-me'),
]
