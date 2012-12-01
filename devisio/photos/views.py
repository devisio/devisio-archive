from django.views.generic import ListView

from models import Album


class AlbumListView(ListView):
    model = Album