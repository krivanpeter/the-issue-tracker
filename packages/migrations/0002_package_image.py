# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-08-25 07:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='image',
            field=models.ImageField(null=True, upload_to='package_images'),
        ),
    ]
