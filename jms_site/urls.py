from django.conf.urls import url
from .views import get_index, get_robots, get_about, get_sitemap, get_contact, get_service, get_services, get_testimonials, get_gallery
urlpatterns = [


    # Home Page
    url(r'^$', get_index, name='home'),


    # About Page
    url(r'^about/$', get_about, name='about'),

    # Services Page
    url(r'^services/$', get_services, name='services'),

    # Service Page
    url(r'^services/(?P<service_slug>[\w-]+)/$', get_service, name='service'),
    url(r'^services/(?P<service_slug>[\w-]+)/essex/', get_service),
    url(r'^services/(?P<service_slug>[\w-]+)/basildon/$', get_service),
    url(r'^services/(?P<service_slug>[\w-]+)/rayleigh/$', get_service),
    url(r'^services/(?P<service_slug>[\w-]+)/benfleet/$', get_service),
    url(r'^services/(?P<service_slug>[\w-]+)/hockley/$', get_service),
    url(r'^services/(?P<service_slug>[\w-]+)/southend/$', get_service),

    url(r'^office-cleaning-essex/$', get_index),
    url(r'^office-cleaning-southend/$', get_index),
    url(r'^commercial-cleaning-essex/$', get_index),
    url(r'^commercial-cleaning-southend/$', get_index),
    url(r'^end-of-tenancy-cleaning-essex/$', get_index),
    url(r'^end-of-tenancy-cleaning-southend/$', get_index),

    # Testimonials Page
    url(r'^testimonials/$', get_testimonials, name='testimonials'),

    # Gallery Page
    url(r'^gallery/$', get_gallery, name='gallery'),

    # Contact Page
    url(r'^contact/$', get_contact, name='contact'),

    url(r'^sitemap.xml/$', get_sitemap),
    url(r'^robots.txt/$', get_robots)
]