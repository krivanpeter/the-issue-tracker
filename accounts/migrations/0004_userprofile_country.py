# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-09-25 15:14
from __future__ import unicode_literals

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_userprofile_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='country',
            field=django_countries.fields.CountryField(max_length=2, null=True),
        ),
    ]