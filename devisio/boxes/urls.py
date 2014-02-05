from django.conf.urls import patterns, url

from devisio.boxes.views import BoxListView

urlpatterns = patterns('',
    url(r'^$', BoxListView.as_view(), name='list'),
)
