from django.utils import timezone
from django.db import models

class Product(models.Model):
    brand = models.CharField(max_length=100)
    title = models.CharField("Название продукта", max_length=255)
    description = models.TextField('Описание продукта')
    price = models.FloatField("Цена")
    date_added = models.DateTimeField("Дата публикации", default=timezone.now)

class Account(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(default='')
    password = models.CharField(max_length=100)

class Enter_code(models.Model):
    entered_code = models.CharField('Код подтверждения ', max_length=6)

class Card_Number(models.Model):
    card_number = models.CharField(max_length=19)