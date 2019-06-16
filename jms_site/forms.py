from django.forms.models import ModelForm

from .models import ContactRequest, Service

class ContactForm(ModelForm):
    class Meta:
        model = ContactRequest
        fields = ['name', 'number', 'email', 'service', 'message']