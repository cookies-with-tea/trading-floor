from django.db import models
from django_postgres_extensions.models.fields import ArrayField

from apps.user.models import User


class Image(models.Model):
    image = models.ImageField(verbose_name='Картинка')
    advertisement = models.ForeignKey(
        'Advertisement',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='images',
    )

    def __str__(self):
        return f'{self.advertisement} | {self.image.name}'

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class AdvertisementCategory(models.Model):
    title = models.TextField(unique=True)

    def __str__(self) -> str:
        return str(self.title)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Advertisement(models.Model):
    URGENCY_LIST = (
        ('URGENT', 'Срочно'),
        ('NSU', 'Не очень срочно'),
        ('NAAU', 'Совсем не срочно'),
    )

    TYPE_LIST = (
        ('EXCHANGE', 'Обмен'),
        ('SELL', 'Продам'),
        ('BUY', 'Куплю'),
        ('GIVE', 'Отдам'),
        ('TAKE', 'Возьму'),
    )

    title = models.TextField('Название')
    description = models.TextField('Описание', blank=True)
    category = models.ForeignKey(AdvertisementCategory, verbose_name='Категория', on_delete=models.CASCADE)
    advertisement_type = ArrayField(models.CharField(max_length=8, choices=TYPE_LIST))
    urgency_type = models.CharField('Срочность объявления', max_length=6, choices=URGENCY_LIST)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
