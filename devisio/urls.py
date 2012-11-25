from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='devisio/home.html'), name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='devisio/about.html'), name='about'),
    url(r'^members/$', TemplateView.as_view(template_name='devisio/members.html'), name='members'),
    url(r'^contact/$', TemplateView.as_view(template_name='devisio/contact.html'), name='contact'),

    # admin
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
