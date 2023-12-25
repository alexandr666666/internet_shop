from django.utils import timezone
from django.db import models

class Product(models.Model):
    image = models.ImageField(default='', upload_to='Изображения/')
    brand = models.CharField(max_length=100)
    title = models.CharField("Название продукта", max_length=255)
    description = models.TextField('Описание продукта')
    price = models.FloatField("Цена")
    date_added = models.DateTimeField("Дата публикации", default=timezone.now)


class Account(models.Model):
    username = models.CharField('Имя пользователя', max_length=100)
    email = models.EmailField("Электронная почта", default='')
    password = models.CharField("Пароль", max_length=100)

class Enter_code(models.Model):
    entered_code = models.CharField('Код подтверждения', max_length=6)

class New_Password(models.Model):
    username = models.CharField('Имя пользователя', max_length=100)
    email = models.EmailField('Электронная почта', default='')
    enter_new_password = models.CharField('Новый пароль', max_length=100)