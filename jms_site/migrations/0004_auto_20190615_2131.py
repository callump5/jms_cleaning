# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-06-15 21:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jms_site', '0003_service_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('before_img_1', models.ImageField(blank=True, null=True, upload_to='job_post/before')),
                ('before_img_2', models.ImageField(blank=True, null=True, upload_to='job_post/before')),
                ('before_img_3', models.ImageField(blank=True, null=True, upload_to='job_post/before')),
                ('after_img_1', models.ImageField(blank=True, null=True, upload_to='job_post/after')),
                ('after_img_2', models.ImageField(blank=True, null=True, upload_to='job_post/after')),
                ('after_img_3', models.ImageField(blank=True, null=True, upload_to='job_post/after')),
            ],
            options={
                'verbose_name': 'Job Post',
                'verbose_name_plural': 'Job Posts',
            },
        ),
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Anonymous', max_length=200)),
                ('company', models.CharField(blank=True, max_length=400, null=True)),
                ('testimonial', models.TextField()),
            ],
            options={
                'verbose_name': 'Testimonial',
                'verbose_name_plural': 'Testimonails',
            },
        ),
        migrations.AddField(
            model_name='jobpost',
            name='testimonial',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jms_site.Testimonials'),
        ),
    ]
