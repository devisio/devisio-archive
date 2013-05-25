import os
import re
import shutil

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save, post_delete

from filebrowser.settings import MEDIA_ROOT, DIRECTORY
from filebrowser.fields import FileBrowseField
from filebrowser.signals import filebrowser_post_upload


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
        if os.path.exists(folder):
            shutil.rmtree(folder)

    def get_photos(self):
        folder = self.get_absolute_path()
        files = os.listdir(folder)
        return files

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['-date']


class Photo(models.Model):
    album = models.ForeignKey(Album, related_name='photos')
    position = models.PositiveSmallIntegerField(default=1)
    image = FileBrowseField(max_length=200)

    def __unicode__(self):
        return u'{0} in {1}'.format(self.image, self.album)


def post_album_delete(sender, instance, using, **kwargs):
    instance.remove_folder()

post_delete.connect(post_album_delete, sender=Album)


def post_album_save(sender, instance, created, raw, using, update_fields, **kwargs):
    instance.create_folder()

post_save.connect(post_album_save, sender=Album)


def post_photo_upload(sender, **kwargs):
    parts = re.split('/', sender.GET['folder'])
    album_id = parts[:2][1]
    try:
        album = Album.objects.get(id=album_id)
        image = kwargs['file']
        if not Photo.objects.filter(image=image).exists():
            photo = Photo.objects.create(album=album, image=image)
            photo.save()
    except Album.DoesNotExist:
        pass

filebrowser_post_upload.connect(post_photo_upload)
