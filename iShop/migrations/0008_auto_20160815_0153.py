# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-14 22:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iShop', '0007_auto_20160815_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='shops',
            field=models.ManyToManyField(null=True, to='iShop.Shop'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='date_start',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 15, 1, 53, 59, 675000)),
        ),
    ]
