# Generated by Django 2.2.24 on 2021-12-27 03:20

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name='作成日'),
        ),
        migrations.AddField(
            model_name='post',
            name='meals',
            field=models.IntegerField(default=30, null=True, verbose_name='食事回数'),
        ),
        migrations.AddField(
            model_name='post',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name='作成時間'),
        ),
    ]
