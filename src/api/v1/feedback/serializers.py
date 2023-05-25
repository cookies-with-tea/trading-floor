from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

from apps.feedback.models import Feedback, File


class FileSerializer(serializers.ModelSerializer):
    url = serializers.FileField(source='file')

    class Meta:
        model = File
        fields = [
            'id',
            'url',
        ]


class FeedbackSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=CurrentUserDefault())
    files = serializers.ListField(
        child=serializers.ImageField(
            allow_empty_file=False,
            use_url=False,
        ),
        write_only=True,
    )

    class Meta:
        model = Feedback
        fields = [
            'id',
            'title',
            'description',
            'user',
            'files',
        ]
