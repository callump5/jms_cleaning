# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import reverse
from django.utils.text import slugify
from django.utils.timezone import now

from django.db import models

from tinymce.models import HTMLField

# Create your models here.

# About

class About(models.Model):
    about = HTMLField()

    def __unicode__(self):
        return 'About - ' + str(self.id)

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About Information'




# Services
class Service(models.Model):
    service = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300, default='', editable=False)
    meta = models.TextField()
    brief = HTMLField()
    description = HTMLField()
    image = models.ImageField(upload_to='services')
    popular = models.BooleanField()
    rank = models.IntegerField()

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

# Service Blurb
class ServiceBlurb(models.Model):
    text = HTMLField()

    def __unicode__(self):
        return 'Service - ' + str(self.id)

    class Meta():
        verbose_name = 'Service Blurb'
        verbose_name_plural = 'Service Blurbs'


# Testimonialsa
class Testimonials(models.Model):
    name = models.CharField(max_length=200, default='Anonymous')
    company = models.CharField(max_length=400, blank=True, null=True)
    testimonial = models.TextField()
    date = models.DateField(
        editable=False,
        default=now()
    )

    def __unicode__(self):
        return self.name

    class Meta():
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonails'



# Job Upload
class JobPost(models.Model):
    title = models.CharField(max_length=200)
    service = models.ForeignKey(Service)
    testimonial = models.ForeignKey(Testimonials, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    before_img_1 = models.ImageField(upload_to='job_post/before', blank=True, null=True)
    before_img_2 = models.ImageField(upload_to='job_post/before', blank=True, null=True)
    before_img_3 = models.ImageField(upload_to='job_post/before', blank=True, null=True)
    after_img_1 = models.ImageField (upload_to='job_post/after', blank=True, null=True)
    after_img_2 = models.ImageField (upload_to='job_post/after', blank=True, null=True)
    after_img_3 = models.ImageField (upload_to='job_post/after', blank=True, null=True)

    def __unicode__(self):
        return self.title

    class Meta():
        verbose_name = 'Job Post'
        verbose_name_plural = 'Job Posts'



# Contact Request
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