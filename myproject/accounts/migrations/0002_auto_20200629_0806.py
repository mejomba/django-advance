# Generated by Django 3.0.7 on 2020-06-29 03:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_author',
            field=models.BooleanField(default=False, verbose_name='نویسنده است'),
        ),
        migrations.AddField(
            model_name='user',
            name='spesial_user',
            field=models.DateTimeField(default=django.utils.timezone.localtime, verbose_name='کاریر ویژه تا'),
        ),
    ]
