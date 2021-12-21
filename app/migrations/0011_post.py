# Generated by Django 2.2.24 on 2021-12-18 22:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20211216_1220'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal_no', models.CharField(max_length=255, verbose_name='食事_No.')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.MainCategory', verbose_name='メニュー名')),
            ],
        ),
    ]
