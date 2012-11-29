from django.conf import settings
from django.db import models

from filebrowser.fields import FileBrowseField


class Album(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    create_date = models.DateTimeField(auto_now_add=True, editable=False)
    edit_date = models.DateTimeField(auto_now=True, editable=False)

class Photo(models.Model):
    album = models.ForeignKey(Album)
    image = FileBrowseField(max_length=200)

    def get_directory(self):
        return u'albums/' + unicode(self.album)
