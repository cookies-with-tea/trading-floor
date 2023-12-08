from rest_framework import routers

from api.v1.deal.views import DealModelViewSet, FeedBackModelViewSet

router = routers.SimpleRouter()
router.register('feedback', FeedBackModelViewSet, basename='feedbacks')
router.register('', DealModelViewSet, basename='deals')

urlpatterns = [] + router.urls
