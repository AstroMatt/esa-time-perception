# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 19:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_v2', '0017_auto_20170828_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trial',
            name='polarization',
            field=models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name='Polarization'),
        ),
    ]