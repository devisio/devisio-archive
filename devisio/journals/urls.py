from django.conf.urls import patterns, url

from devisio.journals.views import JournalsListView


urlpatterns = patterns('',
    url(r'^$', JournalsListView.as_view(), name='list'),
)
