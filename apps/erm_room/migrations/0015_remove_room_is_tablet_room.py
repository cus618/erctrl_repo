# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-27 10:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erm_room', '0014_room_is_tablet_room'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='is_tablet_room',
        ),
    ]