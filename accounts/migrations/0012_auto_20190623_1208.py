# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-23 11:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20190623_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(default='../media/profile_images/male_def.png', upload_to='profile_images'),
        ),
    ]