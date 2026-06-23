from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    image = models.ImageField(upload_to = 'users_images/', blank=True, null=True, verbose_name="Аватар")#Тут задаємо налаштування аватарці профілю
    class Meta:
        db_table: str = "User"
        verbose_name = "Пользователя"
        verbose_name_plural = "Пользователи"
    def __str__(self):
        return self.username




