from django.conf.urls import url
from .views import get_index, get_about, get_contact, get_service, get_services, get_testimonials, get_gallery
urlpatterns = [


    # Home Page
    url(r'^$', get_index, name='home'),

    # About Page
    url(r'about/$', get_about, name='about'),

    # Services Page
    url(r'^services/$', get_services, name='services'),
    # Service Page
    url(r'^services/(?P<service_slug>[\w-]+)/$', get_service, name='service'),

    # Testimonials Page
    url(r'^testimonials/$', get_testimonials, name='testimonials'),

    # Gallery Page
    url(r'^gallery/$', get_gallery, name='gallery'),

    # Contact Page
    url(r'contact/$', get_contact, name='contact')
]