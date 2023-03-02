from django.urls import path

from apps.user.views import UserProfileAPIUpdate

urlpatterns = [
    path('<int:pk>', UserProfileAPIUpdate.as_view()),
]
