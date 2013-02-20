from django.conf.urls import patterns, url

from views import AlbumDetailView, AlbumListView

urlpatterns = patterns('',
    url('^$', AlbumListView.as_view(), name='list'),
    url('^albums/(?P<pk>\d+)/$', AlbumDetailView.as_view(), name='detail'),
)
