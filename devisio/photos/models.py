import os

from django.conf import settings
from django.db import models
from django.utils import timezone

from filebrowser.settings import MEDIA_ROOT, DIRECTORY
from filebrowser.fields import FileBrowseField


class Album(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False)
    date = models.DateField(default=timezone.now())
    visible = models.BooleanField(default=True)

    def get_path(self):
        return u'albums/{0}/'.format(self.id)

    def get_absolute_path(self):
        absolute_path = os.path.join(MEDIA_ROOT, DIRECTORY)
        return os.path.join(absolute_path, self.get_path())

    def create_folder(self):
        folder = self.get_absolute_path()
        if not os.path.exists(folder):
            os.makedirs(folder)

    def remove_folder(self):
        folder = self.get_absolute_path()
        os.rmdir(folder)

    def __unicode__(self):
        return self.name


class Photo(models.Model):
    album = models.ForeignKey(Album)
    image = FileBrowseField(max_length=200)

    def __unicode__(self):
        return u'{0} in {1}'.format(self.image, self.album)
