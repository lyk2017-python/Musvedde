# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-03 13:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_auto_20170803_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='sub_level',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]