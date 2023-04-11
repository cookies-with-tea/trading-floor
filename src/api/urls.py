from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('v1/', include(('api.v1.urls', 'v1'))),
    path('', include('api.common.urls')),
]
