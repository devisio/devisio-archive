import os
from datetime import datetime

from django.conf import settings
from django.db import models

from filebrowser.fields import FileBrowseField


class Journal(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    location = models.CharField(max_length=255)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False)

    def __unicode__(self):
        return self.name


class JournalEntry(models.Model):
    journal = models.ForeignKey(Journal, related_name='entries')
    headline = models.CharField(max_length=255)
    text = models.TextField(blank=True)
    location = models.CharField(max_length=255)
    datetime = models.DateTimeField(default=datetime.now())
    photos = FileBrowseField(max_length=200)

    def get_photos(self):
        return os.listdir(os.path.join(settings.MEDIA_ROOT, self.photos.path))


    class Meta:
        verbose_name = "Journal entry"
        verbose_name_plural = "Journal entries"

