from django.urls import path

from .views import MeAPIView, SignUpAPIView, UserProfileAPIView

urlpatterns = [
    path('<int:pk>', UserProfileAPIView.as_view()),
    path('me', MeAPIView.as_view()),
    path('', SignUpAPIView.as_view()),
]
