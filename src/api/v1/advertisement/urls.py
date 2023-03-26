from django.urls import path

from api.v1.advertisement.views import CreateAdvertisementAPIView

urlpatterns = [
    path('create', CreateAdvertisementAPIView.as_view(), name='create-advertisement'),
]
