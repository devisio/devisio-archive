from django.conf.urls import patterns, url

from devisio.journals.views import JournalsListView, JournalsTeaserView


urlpatterns = patterns('',
    url(r'^$', JournalsTeaserView.as_view(), name='teaser'),
    url(r'^list/$', JournalsListView.as_view(), name='list'),
)
