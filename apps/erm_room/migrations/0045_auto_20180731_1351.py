# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-31 13:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erm_room', '0044_auto_20180719_0846'),
    ]

    operations = [
        migrations.AddField(
            model_name='puzzleclue',
            name='created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='puzzleclue',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
