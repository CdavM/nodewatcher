# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-11 12:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20160311_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='is_default',
            field=models.BooleanField(default=False),
        ),
    ]