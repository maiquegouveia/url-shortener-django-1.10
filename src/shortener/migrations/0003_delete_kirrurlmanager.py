# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2023-03-07 01:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_auto_20230304_2126'),
    ]

    operations = [
        migrations.DeleteModel(
            name='KirrURLManager',
        ),
    ]
