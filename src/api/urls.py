from django.urls import include, path

urlpatterns = [
    path('users/', include('api.v1.user.urls')),
    path('auth/', include('api.common.auth.urls')),
]
