# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-08-25 06:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0003_auto_20190825_0742'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feature',
            name='price',
        ),
    ]
