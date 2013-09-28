from django.conf.urls import patterns, url

from devisio.journals.views import JournalsListView, JournalsDetailView, JournalsTeaserView


urlpatterns = patterns('',
    url(r'^$', JournalsListView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$', JournalsDetailView.as_view(), name='detail'),
    url(r'^teaser/$', JournalsTeaserView.as_view(), name='teaser'),
)
