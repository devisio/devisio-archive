from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

from filebrowser.sites import site


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='devisio/home.html'), name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='devisio/about.html'), name='about'),
    url(r'^members/$', TemplateView.as_view(template_name='devisio/members.html'), name='members'),
    url(r'^contact/$', TemplateView.as_view(template_name='devisio/contact.html'), name='contact'),
    url(r'^imprint/$', TemplateView.as_view(template_name='devisio/imprint.html'), name='imprint'),

    # admin
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
