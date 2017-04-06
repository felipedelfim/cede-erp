# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 21:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashflow', '0006_auto_20170401_0822'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='total',
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=6),
        ),
    ]