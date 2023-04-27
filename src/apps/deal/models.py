from django.db import models

from apps.advertisement.models import Advertisement
from apps.user.models import User


class Deal(models.Model):
    STATUSES = (
        ('OPEN', 'Открыта'),
        ('SUCCESSFULLY_COMPLETED', 'Успешно завершена'),
        ('CANCELLED', 'Отменена'),
    )

    advertisement = models.ForeignKey(
        Advertisement,
        on_delete=models.CASCADE,
        related_name='deals',
        verbose_name='Объявление',
    )
    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='my_deals',
        verbose_name='Продавец',
    )
    buyer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='other_deals',
        verbose_name='Покупатель',
    )
    status = models.CharField(
        'Статус объявления',
        max_length=22,
        choices=STATUSES,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    closed_at = models.DateTimeField(null=True)
    is_response = models.BooleanField(default=False)
