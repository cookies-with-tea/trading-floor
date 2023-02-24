from django.db import models
from multiselectfield import MultiSelectField



class Image(models.Model):
    image = models.ImageField(...)
    advertisement = models.ForeignKey('Advertisement')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

class Advertisement(models.Model):
    URGENCY_LIST = (
        ('URGENT', 'Срочно'),
        ('NOT_SO_URGENT', 'Не очень срочно'),
        ('NOT_AT_ALL_URGENT', 'Совсем не срочно'),
    )

    TYPE_LIST = (
        ('EXCHANGE', 'Обмен'),
        ('SELL', 'Продам'),
        ('BUY', 'Куплю'),
        ('GIVE', 'Отдам'),
        ('TAKE', 'Возьму'),
    )

    title = models.TextField()
    description = models.TextField(blank=True)
    type = MultiSelectField(choices=TYPE_LIST, max_choices=3)
    image = models.ForeignKey('Image', blank=True)
    urgency = models.CharField(max_length=6,
                               choices=URGENCY_LIST)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'