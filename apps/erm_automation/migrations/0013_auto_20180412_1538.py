# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-12 15:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erm_automation', '0012_remove_eventreference_event_max'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='action',
            options={'ordering': ('-id',), 'verbose_name': 'Action', 'verbose_name_plural': 'Actions'},
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ('-id',), 'verbose_name': 'Event', 'verbose_name_plural': 'Events'},
        ),
    ]
