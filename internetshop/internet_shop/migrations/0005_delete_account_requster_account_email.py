# Generated by Django 4.2.7 on 2023-12-02 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internet_shop', '0004_account_requster_alter_account_password_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Account_requster',
        ),
        migrations.AddField(
            model_name='account',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]
