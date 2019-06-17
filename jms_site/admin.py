# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin


from  .models import Service, ContactRequest, Testimonials, JobPost, About

# Register your models here.


admin.site.register(About)
admin.site.register(Service)
admin.site.register(ContactRequest)
admin.site.register(Testimonials)
admin.site.register(JobPost)