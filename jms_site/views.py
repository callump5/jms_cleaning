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

    return render(request, 'base/index.html', args)