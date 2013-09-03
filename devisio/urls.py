from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

from filebrowser.sites import site

from devisio.common.views import AboutView, ContactView, ImprintView


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('devisio.photos.urls', namespace='photos')),
    url(r'^journals/', include('devisio.journals.urls', namespace='journals')),
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^contact/$', ContactView.as_view(), name='contact'),
    url(r'^imprint/$', ImprintView.as_view(), name='imprint'),

    # admin
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
