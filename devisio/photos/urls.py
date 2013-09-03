from django.conf.urls import patterns, url

from views import AlbumJsonDetailView, AlbumListView, OverviewView

urlpatterns = patterns('',
    url(r'^$', AlbumListView.as_view(), name='list'),
    url(r'^overview/$', OverviewView.as_view(), name='overview'),
    url(r'^(?P<slug>[\w-]+)/$', AlbumJsonDetailView.as_view(), name='detail'),
    url(r'^albums/(?P<pk>\d+)/$', AlbumJsonDetailView.as_view(), name='detail'),
)
