from django.conf.urls import url
from .views import get_index, get_about, get_services, get_testimonials, get_gallery, get_policies

urlpatterns = [


    # Home Page
    url(r'^$', get_index, name='home'),

    # About Page
    url(r'about/$', get_about, name='about'),

    # Service Page
    url(r'^services/$', get_services, name='services'),

    # Testimonials Page
    url(r'^testimonials/$', get_testimonials, name='testimonials'),

    # Gallery Page
    url(r'^gallery/$', get_gallery, name='gallery'),

    # Policies Page
    url(r'policies/$', get_policies, name='policies')
]