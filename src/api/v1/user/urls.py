from django.urls import path

from .views import UserProfileAPICreate, UserProfileAPIRetrieve, UserProfileAPIUpdateDestroy

urlpatterns = [
    path('<int:pk>', UserProfileAPIRetrieve.as_view()),
    path('me', UserProfileAPIUpdateDestroy.as_view()),
    path('sign-up', UserProfileAPICreate.as_view()),
]
