from django.db import models

from apps.user.models import User


class File(models.Model):
    file = models.FileField(verbose_name='Файл')
    feedback = models.ForeignKey(
        'Feedback',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='files',
    )

    def __str__(self):
        return f'{self.feedback} | {self.file.name}'

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'


class Feedback(models.Model):
    title = models.TextField()
    description = models.TextField()
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='my_feedbacks',
        verbose_name='Автор',
    )
