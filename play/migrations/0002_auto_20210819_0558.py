# Generated by Django 3.2.6 on 2021-08-19 05:58

from django.db import migrations, models
import play.models


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='photo',
            field=models.ImageField(blank=True, default='field_default.jpg', upload_to=play.models.media_path),
        ),
        migrations.AlterField(
            model_name='player',
            name='photo',
            field=models.ImageField(blank=True, default='avatar_default.png', upload_to=play.models.media_path),
        ),
    ]