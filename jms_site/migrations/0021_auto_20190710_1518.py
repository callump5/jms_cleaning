# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-07-10 15:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jms_site', '0020_auto_20190622_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonials',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 7, 10, 15, 18, 33, 678844, tzinfo=utc), editable=False),
        ),
    ]
