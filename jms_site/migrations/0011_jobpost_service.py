# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-17 13:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jms_site', '0010_delete_testimonialblurb'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='service',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='jms_site.Service'),
            preserve_default=False,
        ),
    ]
