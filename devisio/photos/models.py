from django.conf import settings
from django.db import models
from django.utils import timezone


from filebrowser.fields import FileBrowseField


class Album(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False)
    date = models.DateField(default=timezone.now())

    def __unicode__(self):
        return self.name


class Photo(models.Model):
    album = models.ForeignKey(Album)
    image = FileBrowseField(max_length=200)

    def get_directory(self):
        return u'albums/' + unicode(self.album)

    def __unicode__(self):
        return u'{0} in {1}'.format(self.image, self.album)
