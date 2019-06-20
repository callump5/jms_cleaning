from django.conf.urls import url
from .views import get_index, get_about, get_sitemap, get_robots, get_contact, get_service, get_services, get_testimonials, get_gallery
urlpatterns = [


    # Home Page
    url(r'^$', get_index, name='home'),
    url(r'^office-cleaning-essex/$', get_index),
    url(r'^office-cleaning-southend/$', get_index),
    url(r'^office-cleaning-rayleigh/$', get_index),
    url(r'^office-cleaning-benfleet/$', get_index),
    url(r'^office-cleaning-westcliff/$', get_index),
    url(r'^office-cleaning-leigh/$', get_index),
    url(r'^commercial-cleaning-essex/$', get_index),
    url(r'^commercial-cleaning-southend/$', get_index),
    url(r'^commercial-cleaning-rayleigh/$', get_index),
    url(r'^commercial-cleaning-benfleet/$', get_index),
    url(r'^commercial-cleaning-westcliff/$', get_index),
    url(r'^commercial-cleaning-leigh/$', get_index),
    url(r'^cleaning-service-essex/$', get_index),
    url(r'^cleaning-service-southend/$', get_index),
    url(r'^cleaning-service-rayleigh/$', get_index),
    url(r'^cleaning-service-benfleet/$', get_index),
    url(r'^cleaning-service-westcliff/$', get_index),
    url(r'^cleaning-service-leigh/$', get_index),
    url(r'^end-of-tenancy-cleaning-essex/$', get_index),
    url(r'^end-of-tenancy-cleaning-southend/$', get_index),
    url(r'^end-of-tenancy-cleaning-rayleigh/$', get_index),
    url(r'^end-of-tenancy-cleaning-benfleet/$', get_index),
    url(r'^end-of-tenancy-cleaning-westcliff/$', get_index),
    url(r'^end-of-tenancy-cleaning-leigh/$', get_index),

    # About Page
    url(r'^about/$', get_about, name='about'),

    # Services Page
    url(r'^services/$', get_services, name='services'),
    # Service Page
    url(r'^services/(?P<service_slug>[\w-]+)/$', get_service, name='service'),

    # Testimonials Page
    url(r'^testimonials/$', get_testimonials, name='testimonials'),

    # Gallery Page
    url(r'^gallery/$', get_gallery, name='gallery'),

    # Contact Page
    url(r'contact/$', get_contact, name='contact'),


    url(r'^sitemap.xml/$', get_sitemap),
    url(r'^robots.txt/$', get_robots),
]