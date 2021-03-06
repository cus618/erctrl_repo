# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-10-04 10:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import picklefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('erm_room', '0046_auto_20180731_1353'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhilipGroupsAndScenes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                ('bridge_url', models.CharField(blank=True, max_length=255, null=True)),
                ('settings_data', picklefield.fields.PickledObjectField(default={}, editable=False)),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='room_philip_group_and_scene', to='erm_room.Room')),
            ],
        ),
    ]
