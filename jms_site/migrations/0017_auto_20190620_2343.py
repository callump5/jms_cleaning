# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-20 22:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jms_site', '0016_auto_20190620_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonials',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 6, 20, 22, 43, 42, 649000, tzinfo=utc), editable=False),
        ),
    ]
