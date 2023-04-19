from django.contrib import admin

from .models import Advertisement, AdvertisementCategory, Image

admin.site.register(Advertisement)
admin.site.register(AdvertisementCategory)
admin.site.register(Image)
