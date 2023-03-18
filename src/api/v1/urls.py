from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.versioning import NamespaceVersioning

urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(versioning_class=NamespaceVersioning, api_version='v1'), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),
    path('users/', include('api.v1.user.urls')),
]
