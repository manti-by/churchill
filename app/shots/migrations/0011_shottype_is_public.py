# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-11 15:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shots', '0010_auto_20161111_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='shottype',
            name='is_public',
            field=models.BooleanField(default=False),
        ),
    ]
