from django.views.generic import DetailView, ListView

from models import Album


class AlbumListView(ListView):
    model = Album


class AlbumDetailView(DetailView):
    model = Album
