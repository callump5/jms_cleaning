# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .forms import ContactForm
from .models import Service

# Create your views here.

def get_index(request):

    services = Service.objects.all()

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Thanks for getting in touch! We will try to contact you as soon as possible!')
            return redirect('home')
        else:
            contact_form = ContactForm()

    else:
        contact_form = ContactForm()

    args = {
        'services': services,
        'contact_form': contact_form,
    }

    return render(request, 'home/home.html', args)

def get_about(request):
    return render(request, 'about/about_page.html')

def get_services(request):
    return render(request, 'services/services_page.html')

def get_testimonials(request):
    return render(request, 'testimonials/testimonials_page.html')

def get_gallery(request):
    return render(request, 'gallery/gallery_page.html')

def get_policies(request):
    return render(request, 'policies/policies.html')