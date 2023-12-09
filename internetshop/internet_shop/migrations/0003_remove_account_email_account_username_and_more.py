# Generated by Django 4.2.7 on 2023-11-30 16:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('internet_shop', '0002_account_alter_product_date_added_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='email',
        ),
        migrations.AddField(
            model_name='account',
            name='username',
            field=models.CharField(default='Unknown', max_length=100, verbose_name='Имя пользователя'),
        ),
        migrations.AlterField(
            model_name='account',
            name='password',
            field=models.CharField(max_length=100, verbose_name='Пароль'),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_added',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата публикации'),
        ),
    ]