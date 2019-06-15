# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 12:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import erm_room.models


class Migration(migrations.Migration):

    dependencies = [
        ('erm_room', '0002_clue'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_name', models.FileField(max_length=255, upload_to=erm_room.models.get_upload_path)),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='room_images', to='erm_room.Room')),
            ],
            options={
                'verbose_name': 'RoomImage',
                'verbose_name_plural': 'RoomImages',
            },
        ),
    ]
