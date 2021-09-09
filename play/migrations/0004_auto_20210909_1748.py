# Generated by Django 3.2.6 on 2021-09-09 22:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('play', '0003_auto_20210909_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='address',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fields', to='play.addressfield'),
        ),
        migrations.AlterField(
            model_name='field',
            name='fields_services',
            field=models.ManyToManyField(blank=True, null=True, related_name='fields', to='play.Service'),
        ),
        migrations.AlterField(
            model_name='field',
            name='football_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fields', to='play.footballtype'),
        ),
        migrations.AlterField(
            model_name='field',
            name='rent_cost',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
