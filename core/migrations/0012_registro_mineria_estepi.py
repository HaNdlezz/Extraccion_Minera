# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-01-25 20:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20190123_0055'),
    ]

    operations = [
        migrations.AddField(
            model_name='registro_mineria',
            name='estepi',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
