# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-06-20 16:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jms_site', '0015_auto_20190620_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonials',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 6, 20, 16, 7, 49, 889192, tzinfo=utc), editable=False),
        ),
    ]
