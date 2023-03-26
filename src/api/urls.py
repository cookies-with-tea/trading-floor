from django.urls import include, path

urlpatterns = [
    path('v1/users/', include('api.v1.user.urls')),
    path('v1/advertisements/', include('api.v1.advertisement.urls')),
    path('auth/', include('api.common.auth.urls')),
]
