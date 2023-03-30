from rest_framework import routers

from api.v1.advertisement.views import CreateAdvertisementViewSet

router = routers.SimpleRouter()
router.register('advertisements', CreateAdvertisementViewSet)

urlpatterns = [] + router.urls
