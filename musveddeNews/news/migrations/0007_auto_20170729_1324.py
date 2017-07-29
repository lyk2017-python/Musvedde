# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-29 13:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20170729_1323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='reported_count',
        ),
        migrations.AddField(
            model_name='comments',
            name='hidden',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='comments',
            name='reported',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
