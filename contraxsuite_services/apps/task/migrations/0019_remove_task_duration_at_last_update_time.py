# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-06-19 07:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0018_auto_20180615_1423'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='duration_at_last_update_time',
        ),
    ]
