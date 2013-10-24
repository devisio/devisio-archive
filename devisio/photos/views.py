from django.views.generic import DetailView, ListView

from devisio.common.pjax import PJAXResponseMixin
from models import Album
from devisio.photos.utils import serialize_photos_json


class AlbumDetailView(PJAXResponseMixin, DetailView):
    model = Album

    def get_context_data(self, *args, **kwargs):
        context = super(AlbumDetailView, self).get_context_data(*args, **kwargs)
        context['json'] = serialize_photos_json(context['object'].photos.all())
        return context


class AlbumListView(PJAXResponseMixin, ListView):
    def get_queryset(self):
        return Album.objects.visible()[:6]


class AlbumOverviewView(PJAXResponseMixin, ListView):
    template_name = 'photos/album_overview.html'

    def get_queryset(self):
        return Album.objects.visible()
