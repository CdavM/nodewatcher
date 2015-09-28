# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import json_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectconfig',
            name='annotations',
            field=json_field.fields.JSONField(default={}, help_text='Enter a valid JSON object', editable=False),
        ),
    ]