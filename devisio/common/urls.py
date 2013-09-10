from django.conf.urls import patterns, url

from devisio.common.views import AboutView, ContactView, ImprintView


urlpatterns = patterns('',
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^contact/$', ContactView.as_view(), name='contact'),
    url(r'^imprint/$', ImprintView.as_view(), name='imprint'),
)
