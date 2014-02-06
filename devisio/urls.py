from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'devisio.views.home', name='home'),
    url(r'^', include('devisio.boxes.urls', namespace='boxes')),

    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'media\/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
