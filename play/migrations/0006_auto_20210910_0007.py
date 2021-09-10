# Generated by Django 3.2.6 on 2021-09-10 05:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('play', '0005_administrator_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='fields_services',
            field=models.ManyToManyField(blank=True, related_name='fields', to='play.Service'),
        ),
        migrations.AlterField(
            model_name='match',
            name='organizer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='matches', to=settings.AUTH_USER_MODEL),
        ),
    ]
