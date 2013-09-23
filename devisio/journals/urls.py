from django.conf.urls import patterns, url

from devisio.journals.views import JournalsListView, JournalsTeaserView


urlpatterns = patterns('',
    url(r'^$', JournalsListView.as_view(), name='list'),
    url(r'^teaser/$', JournalsTeaserView.as_view(), name='teaser'),
)
