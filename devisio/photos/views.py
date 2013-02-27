from django.http import HttpResponse
from django.utils import simplejson as json
from django.views.generic import ListView
from django.views.generic.detail import BaseDetailView

from models import Album


class AlbumJsonDetailView(BaseDetailView):
    model = Album

    def serialize_album(self, album):
        def _serialize_photo(photo):
            version = photo.image.version_generate('album_gallery')
            return {
                "src": version.url,
                "width": version.width,
                "height": version.height
            }

        res = [_serialize_photo(photo) for photo in album.photos.all()]

        return json.dumps(res)

    def render_to_response(self, context):
        return HttpResponse(self.serialize_album(context['object']), content_type='application/json')


class AlbumListView(ListView):
    model = Album
