from django.urls import path

from .views import UserProfileAPIUpdate

urlpatterns = [path('<int:pk>', UserProfileAPIUpdate.as_view())]
