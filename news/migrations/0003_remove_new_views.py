# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-08-08 16:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20190702_1312'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='new',
            name='views',
        ),
    ]
