from django_filters import rest_framework as filters

from apps.advertisement.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    class Meta:
        model = Advertisement
        fields = ['category', 'author__id', 'is_open']
