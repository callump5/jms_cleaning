# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-16 17:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jms_site', '0005_about'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='about',
        ),
    ]
