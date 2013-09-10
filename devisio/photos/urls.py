from django.conf.urls import patterns, url

from views import AlbumJsonDetailView, AlbumPjaxDetailView, AlbumListView, OverviewView

urlpatterns = patterns('',
    url(r'^$', AlbumListView.as_view(), name='list'),
    url(r'^overview/$', OverviewView.as_view(), name='overview'),
    url(r'^(?P<slug>[\w-]+)/$', AlbumPjaxDetailView.as_view(), name='pjax-detail'),
    url(r'^albums/(?P<pk>\d+)/$', AlbumJsonDetailView.as_view(), name='detail'),
)
