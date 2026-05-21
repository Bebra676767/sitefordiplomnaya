from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator, EmailValidator

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    fio = models.CharField(
        max_length=200,
        verbose_name='ФИО',
        validators=[
            RegexValidator(
                regex=r'^[а-яА-ЯёЁ\s]+$',
                message='ФИО должно содержать только кириллицу и пробелы'
            )
        ]
    )
    phone = models.CharField(
        max_length=18,
        verbose_name='Телефон',
        validators=[
            RegexValidator(
                regex=r'^8\(\d{3}\)\d{3}-\d{2}-\d{2}$',
                message='Телефон должен быть в формате 8(XXX)XXX-XX-XX'
            )
        ]
    )
    
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
    
    def __str__(self):
        return self.fio