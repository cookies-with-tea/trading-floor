from django.contrib import admin

from apps.feedback.models import Feedback, File

admin.site.register(Feedback)
admin.site.register(File)
