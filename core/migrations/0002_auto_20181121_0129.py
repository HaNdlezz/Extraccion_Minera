# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-11-21 01:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registro_mineria',
            name='diario',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='registro_mineria',
            name='texto',
            field=models.TextField(blank=True, max_length=100000, null=True),
        ),
    ]
