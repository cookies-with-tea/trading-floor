from django.db import models
from multiselectfield import MultiSelectField

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
    advertisement_type = MultiSelectField(
        verbose_name='Тип объявления',
        choices=TYPE_LIST,
        max_choices=3,
        max_length=100,
    )
    urgency_type = models.CharField('Срочность объявления', max_length=6, choices=URGENCY_LIST)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
