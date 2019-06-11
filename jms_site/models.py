# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import reverse
from django.utils.text import slugify

from django.db import models

# Create your models here.

class Service(models.Model):
    service = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300, default='', editable=False)
    description = models.TextField()
    image = models.ImageField(upload_to='services')

    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug
        }

    def save(self, *args, **kwargs):
        value = self.service
        self.slug = slugify(value, allow_unicode=True)
        super(Service, self).save(*args, **kwargs)


    def __unicode__(self):
        return self.service

    class Meta():
        verbose_name = "Service"
        verbose_name_plural = 'Services'



class ContactRequest(models.Model):
    name = models.CharField(max_length=200)
    number = models.CharField(max_length=12)
    email = models.EmailField(max_length=200)
    service = models.ForeignKey(Service, related_name='service_request')
    message = models.TextField()

    def __unicode__(self):
        return str(self.service) + 'Request'

    class Meta():
        verbose_name = "Contact Request"
        verbose_name_plural = 'Enquiries'

