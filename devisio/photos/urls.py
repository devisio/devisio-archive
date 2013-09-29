from django.conf.urls import patterns, url

from views import AlbumDetailView, AlbumListView, OverviewView

urlpatterns = patterns('',
    url('^$', AlbumListView.as_view(), name='list'),
    url(r'^overview/$', OverviewView.as_view(), name='overview'),
    url(r'^albums/(?P<slug>[\w-]+)/$', AlbumDetailView.as_view(), name='detail'),
)
