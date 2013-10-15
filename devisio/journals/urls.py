from django.conf.urls import patterns, url

from devisio.journals.views import JournalsListView, JournalsDetailView, JournalsTeaserView, JournalsMapView


urlpatterns = patterns('',
    url(r'^$', JournalsListView.as_view(), name='list'),
    url(r'^map/$', JournalsMapView.as_view(), name='map'),
    url(r'^(?P<slug>[\w-]+)/$', JournalsDetailView.as_view(), name='detail'),
    url(r'^teaser/$', JournalsTeaserView.as_view(), name='teaser'),
)
