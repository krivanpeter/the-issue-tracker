# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-09-13 07:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0016_auto_20190913_0833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='open',
            field=models.CharField(choices=[('open', 'Open'), ('development', 'Under Development'), ('closed', 'Closed')], default='open', max_length=11),
        ),
    ]
