# Generated by Django 3.2.6 on 2021-08-20 04:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0003_auto_20210820_0426'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
