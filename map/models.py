from django.db import models
from django.contrib.auth.models import User





class VerifiedTag(models.Model):
    name = models.CharField('Название', max_length=30)
    description = models.TextField('Описание', max_length=100)
    image = models.ImageField('Изображение', upload_to='images/')
    location = models.CharField('Местоположение', max_length=30)
    x_coord = models.FloatField('Координата X')
    y_coord = models.FloatField('Координата Y')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Метка'
        verbose_name_plural = 'Метки'


class UnverifiedTag(models.Model):
    name = models.CharField('Название', max_length=30)
    description = models.TextField('Описание', max_length=100)
    image = models.ImageField('Изображение', upload_to='images/')
    location = models.CharField('Местоположение', max_length=30)
    x_coord = models.FloatField('Координата X')
    y_coord = models.FloatField('Координата Y')
    username = models.CharField('Имя пользователя', max_length=30)
    email = models.EmailField('Email', max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Метка'
        verbose_name_plural = 'Метки'

