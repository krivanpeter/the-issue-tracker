# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-08-11 08:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0007_auto_20190808_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='title',
            field=models.TextField(default='', max_length=60),
        ),
    ]
