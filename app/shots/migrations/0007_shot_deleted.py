# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-04 13:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shots', '0006_auto_20161104_0915'),
    ]

    operations = [
        migrations.AddField(
            model_name='shot',
            name='deleted',
            field=models.IntegerField(default=0),
        ),
    ]