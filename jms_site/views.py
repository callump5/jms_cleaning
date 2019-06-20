# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from smtplib import SMTPAuthenticationError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .send_email import send_my_mail, authError

from .forms import ContactForm
from .models import About, Service, Testimonials, JobPost, ServiceBlurb

# Create your views here.



# Get Home
def get_index(request):

    about = About.objects.all().first()
    jobs = JobPost.objects.all()

    services = Service.objects.all()
    service_blurb = ServiceBlurb.objects.all().first()

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact = contact_form.save()
            messages.success(request, 'Thanks for getting in touch! We will try to contact you as soon as possible!')
            try:
                send_my_mail(request, contact.name, contact.email, contact.number, contact.service, contact.message)
            except SMTPAuthenticationError:
                authError(request)
            redirect('home')
        else:
            contact_form = ContactForm()

    else:
        contact_form = ContactForm()

    args = {
        'about': about,
        'services': services,
        'jobs': jobs,
        'contact_form': contact_form,
        'service_blurb': service_blurb
    }

    return render(request, 'home/home.html', args)



# About Page
def get_about(request):
    abouts = About.objects.all()

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact = contact_form.save()
            messages.success(request, 'Thanks for getting in touch! We will try to contact you as soon as possible!')
            try:
                send_my_mail(request, contact.name, contact.email, contact.number, contact.service, contact.message)
            except SMTPAuthenticationError:
                authError(request)
            redirect('home')
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
    service_blurbs = ServiceBlurb.objects.all()

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact = contact_form.save()
            messages.success(request, 'Thanks for getting in touch! We will try to contact you as soon as possible!')
            try:
                send_my_mail(request, contact.name, contact.email, contact.number, contact.service, contact.message)
            except SMTPAuthenticationError:
                authError(request)
            redirect('home')
        else:
            contact_form = ContactForm()

    else:
        contact_form = ContactForm()


    args = {
        'services': services,
        'contact_form': contact_form,
        'service_blurbs': service_blurbs
    }

    return render(request, 'services/services_page.html', args)



# Get Service
def get_service(request, service_slug):
    service = get_object_or_404(Service, slug=service_slug)

    jobs = JobPost.objects.filter(service_id=service.id)[:2]

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact = contact_form.save()
            messages.success(request, 'Thanks for getting in touch! We will try to contact you as soon as possible!')
            try:
                send_my_mail(request, contact.name, contact.email, contact.number, contact.service, contact.message)
            except SMTPAuthenticationError:
                authError(request)
            redirect('home')
        else:
            contact_form = ContactForm()

    else:
        contact_form = ContactForm()

    args = {
        'service': service,
        'jobs': jobs,
        'contact_form': contact_form
    }

    return render(request, 'services/service_item_page.html', args)



def get_testimonials(request):

    testimonials = Testimonials.objects.all()
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact = contact_form.save()
            messages.success(request, 'Thanks for getting in touch! We will try to contact you as soon as possible!')
            try:
                send_my_mail(request, contact.name, contact.email, contact.number, contact.service, contact.message)
            except SMTPAuthenticationError:
                authError(request)
            redirect('home')
        else:
            contact_form = ContactForm()

    else:
        contact_form = ContactForm()

    args = {
        'testimonials': testimonials,
        'contact_form': contact_form
    }

    return render(request, 'testimonials/testimonials_page.html', args)



def get_gallery(request):

    jobs = JobPost.objects.all()
    if request.method == 'POST':

        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            contact = contact_form.save()
            messages.success(request, 'Thanks for getting in touch! We will try to contact you as soon as possible!')
            try:
                send_my_mail(request, contact.name, contact.email, contact.number, contact.service, contact.message)
            except SMTPAuthenticationError:
                authError(request)
            redirect('home')
        else:
            contact_form = ContactForm()

    else:
        contact_form = ContactForm()

    args = {
        'jobs':jobs,
        'contact_form': contact_form
    }
    return render(request, 'gallery/gallery_page.html', args)



def get_contact(request):

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact = contact_form.save()
            messages.success(request, 'Thanks for getting in touch! We will try to contact you as soon as possible!')
            try:
                send_my_mail(request, contact.name, contact.email, contact.number, contact.service, contact.message)
            except SMTPAuthenticationError:
                authError(request)
            redirect('home')
        else:
            contact_form = ContactForm()

    else:
        contact_form = ContactForm()

    args = {
        'contact_form': contact_form
    }

    return render(request, 'contact/contact_page.html', args)



def get_robots(request):
    return render(request, 'crawlers/robots.txt')



def get_sitemap(request):
    return render(request, 'crawlers/sitemap-1001909.xml')