# Generated by Django 2.2 on 2020-04-16 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_auto_20200416_1844'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='end_time',
            field=models.TextField(default='00:00:00 00/00/00'),
        ),
        migrations.AddField(
            model_name='event',
            name='start_time',
            field=models.TextField(default='00:00:00 00/00/00'),
        ),
    ]
