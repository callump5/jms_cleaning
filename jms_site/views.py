# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .forms import ContactForm
from .models import About, Service, Testimonials, JobPost

# Create your views here.



# Get Home
def get_index(request):

    about = About.objects.all().first()
    jobs = JobPost.objects.all()

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
        'about': about,
        'services': services,
        'jobs': jobs,
        'contact_form': contact_form,
    }

    return render(request, 'home/home.html', args)



# About Page
def get_about(request):
    abouts = About.objects.all()
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
        'abouts': abouts,
        'contact_form': contact_form,
    }

    return render(request, 'about/about_page.html', args)


# Services Page
def get_services(request):

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
    return render(request, 'services/services_page.html', args)


# Get Service
def get_service(request, service_slug):
    service = get_object_or_404(Service, slug=service_slug)

    jobs = JobPost.objects.filter(service_id=service.id)[:3]

    args = {
        'service': service,
        'jobs': jobs
    }
    return render(request, 'services/service_item_page.html', args)

def get_testimonials(request):

    testimonials = Testimonials.objects.all()

    args = {
        'testimonials': testimonials
    }
    return render(request, 'testimonials/testimonials_page.html', args)

def get_gallery(request):

    jobs = JobPost.objects.all()

    args = {
        'jobs':jobs
    }
    return render(request, 'gallery/gallery_page.html', args)

def get_contact(request):
    return render(request, 'contact/contact_page.html')