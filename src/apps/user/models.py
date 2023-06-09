from colorfield.fields import ColorField
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.exceptions import ValidationError
from django.db import models
from imagekit.models import ProcessedImageField
from pilkit.processors import ResizeToFill

from config.settings import EMAIL_DOMAIN
from utils.colors import generate_random_color
from utils.strings import is_correct_email_domain


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, password, room_number, last_name=None):
        if not email:
            raise TypeError('The "email" field is required')
        if not first_name:
            raise TypeError('The "first name" field is required')
        if not password:
            raise TypeError('The "password" field is required')
        if not room_number:
            raise TypeError('The "room number" field is required')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            room_number=room_number,
        )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, first_name, password):
        user = self.create_user(email, first_name, password, room_number=666)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save()

        return user


def validate_email_address(email: str) -> None:
    if not is_correct_email_domain(email, EMAIL_DOMAIN):
        raise ValidationError('Разрешены только адреса домена mer.ci.nsu.ru')


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('Почта', unique=True, db_index=True, validators=[validate_email_address])
    first_name = models.CharField('Имя', max_length=20)
    last_name = models.CharField('Фамилия', max_length=20, blank=True, null=True)
    room_number = models.PositiveIntegerField('Номер комнаты', null=True)
    avatar = ProcessedImageField(
        format='PNG',
        processors=[
            ResizeToFill(50, 50),
        ],
        verbose_name='Аватарка пользователя',
        blank=True,
        null=True,
    )
    avatar_color = ColorField(verbose_name='Цвет аватарки', default=generate_random_color, null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата обновления', auto_now=True)

    telegram_username = models.TextField(verbose_name='Имя пользователя в Telegram', blank=True, null=True)
    vk_username = models.TextField(verbose_name='Имя пользователя в VK', blank=True, null=True)

    is_active = models.BooleanField(verbose_name='Активен ли пользователь?', default=True)
    is_staff = models.BooleanField(verbose_name='Пользователь является администратором?', default=False)
    is_register = models.BooleanField(verbose_name='Пользователь зарегистрирован?', default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
