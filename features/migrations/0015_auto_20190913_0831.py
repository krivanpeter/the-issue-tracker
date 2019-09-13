# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-09-13 07:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0014_auto_20190912_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='open',
            field=models.CharField(choices=[('O', 'Open'), ('D', 'Under Development'), ('C', 'Closed')], default='Open', max_length=1),
        ),
    ]
