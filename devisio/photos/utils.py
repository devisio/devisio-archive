from django.utils import simplejson as json


def serialize_photos_json(queryset):
    def _serialize_photo(photo):
        version = photo.image.version_generate('album_gallery')
        return {
            "src": version.url,
            "width": version.width,
            "height": version.height
        }

    res = [_serialize_photo(photo) for photo in queryset]

    return json.dumps(res)
