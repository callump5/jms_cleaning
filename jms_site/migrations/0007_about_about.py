# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-16 17:02
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('jms_site', '0006_remove_about_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='about',
            field=tinymce.models.HTMLField(default='aseg'),
            preserve_default=False,
        ),
    ]
