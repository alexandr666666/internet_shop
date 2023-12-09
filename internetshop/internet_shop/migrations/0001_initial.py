# Generated by Django 4.2.7 on 2023-11-26 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('date_added', models.DateTimeField()),
            ],
        ),
    ]
