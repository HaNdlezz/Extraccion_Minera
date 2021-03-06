# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-11-23 04:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20181121_0129'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50)),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='registro_mineria',
            name='diario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Diario'),
        ),
    ]
