from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from imagekit.models import ProcessedImageField
from pilkit.processors import ResizeToFill


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, password, room_number, last_name=None):
        if not email:
            raise TypeError('Поле "email" является обязательным')
        if not first_name:
            raise TypeError('Поле "first name" является обязательным')
        if not password:
            raise TypeError('Поле "password" является обязательным')
        if not room_number:
            raise TypeError('Поле "room number" является обязательным')

        user = self.model(username=first_name + last_name, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(email, username, password, room_number=666)
        user.is_superuser = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.CharField('email', max_length=100, unique=True, db_index=True)
    first_name = models.CharField('first_name', max_length=20, unique=True)
    avatar = ProcessedImageField(
        format='PNG',
        processors=[
            ResizeToFill(50, 50),
        ],
        verbose_name='Аватарка пользователя',
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
