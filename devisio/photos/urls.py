from django.conf.urls import patterns, url

from views import AlbumJsonDetailView, AlbumListView

urlpatterns = patterns('',
    url('^$', AlbumListView.as_view(), name='list'),
    url('^albums/(?P<pk>\d+)/$', AlbumJsonDetailView.as_view(), name='detail'),
)
