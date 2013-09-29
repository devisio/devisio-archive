from django.conf.urls import patterns, url

from views import AlbumDetailView, AlbumListView, AlbumOverviewView

urlpatterns = patterns('',
    url(r'^$', AlbumListView.as_view(), name='list'),
    url(r'^overview/$', AlbumOverviewView.as_view(), name='overview'),
    url(r'^albums/(?P<slug>[\w-]+)/$', AlbumDetailView.as_view(), name='detail'),
)
