from django.urls import path

from .views import UserProfileAPIList

urlpatterns = [
    path('all-users', UserProfileAPIList.as_view()),
]
