from django.db import models
from django.contrib.auth.models import User

from filebrowser.fields import FileBrowseField


class Album(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User)
    create_date = models.DateTimeField(auto_now_add=True, editable=False)
    edit_date = models.DateTimeField(auto_now=True, editable=False)

class Photo(models.Model):
    album = models.ForeignKey(Album)
    image = FileBrowseField()

    def get_directory(self):
        return u'albums/' + unicode(self.album)
