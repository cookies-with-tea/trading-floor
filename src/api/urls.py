from django.urls import include, path

urlpatterns = [
    path('v1/', include(('api.v1.urls', 'v1'))),
    path('', include('api.common.urls')),
]
