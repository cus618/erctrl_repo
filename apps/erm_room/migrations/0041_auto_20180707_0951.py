# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-07 09:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erm_room', '0040_auto_20180707_0719'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='fail_ending_type',
            field=models.CharField(choices=[('Video Ending', 'video ending'), ('Text Ending', 'text ending')], default='video ending', max_length=255),
        ),
        migrations.AddField(
            model_name='room',
            name='success_ending_type',
            field=models.CharField(choices=[('Video Ending', 'video ending'), ('Text Ending', 'text ending')], default='video ending', max_length=255),
        ),
    ]
