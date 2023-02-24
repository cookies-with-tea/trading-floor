from django.db import models


class Type(models.Model):
    title = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тип объявления'
        verbose_name_plural = 'Типы объявлений'


class Image(models.Model):
    image = models.ImageField(verbose_name='Картинка')
    advertisement = models.ForeignKey('Advertisement', verbose_name='Объявление', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.advertisement} | {self.image.name}'

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class Advertisement(models.Model):
    title = models.TextField()
    description = models.TextField(blank=True)
    type = models.ManyToManyField(Type)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
