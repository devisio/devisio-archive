from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

from filebrowser.sites import site

from devisio.common.views import GoogleVerification



admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('devisio.photos.urls', namespace='photos')),
    url(r'^journals/', include('devisio.journals.urls', namespace='journals')),
    url(r'^', include('devisio.common.urls', namespace='common')),
    url(r'^google597cf5de6df346e6.html$', GoogleVerification.as_view(), name='google-verification'),

    # admin
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
