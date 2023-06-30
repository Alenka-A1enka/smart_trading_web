from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'

class Users(models.Model):
    surname = models.CharField('Фамилия', max_length=100)
    name = models.CharField('Имя', max_length=100)
    phone_number = models.CharField('Номер телефона', max_length=15)

    def __str__(self):
        return f'{self.surname} {self.name} ({self.phone_number})'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


