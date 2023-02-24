from django.db import models


class Type(models.Model):
    title = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тип объявления'
        verbose_name_plural = 'Типы объявлений'


class Image(models.Model):
    image = models.ImageField(...)
    advertisement = models.ForeignKey('Advertisement')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

class Advertisement(models.Model):
    title = models.TextField()
    description = models.TextField(blank=True)
    type = models.ManyToManyField(Type)
    image = models.ForeignKey('Image')
    urgency = models.Choices(...)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'