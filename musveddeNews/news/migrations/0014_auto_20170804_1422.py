# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-04 11:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0013_post_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='user_email',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='user_name',
        ),
        migrations.AddField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]