from rest_framework import routers

from api.v1.advertisement.views import AdvertisementModelViewSet

router = routers.SimpleRouter()
router.register('', AdvertisementModelViewSet, basename='advertisements')

urlpatterns = [] + router.urls
