# Generated by Django 4.0.2 on 2023-01-05 15:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_alter_room_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='time',
            field=models.TimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
