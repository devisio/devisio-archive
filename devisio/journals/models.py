from datetime import datetime

from django.conf import settings
from django.db import models

from filebrowser.fields import FileBrowseField


class JournalManager(models.Manager):
    def get_valid(self):
        return self.filter(entries__photos__highlight=True)


class Journal(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    location = models.CharField(max_length=255)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False)

    objects = JournalManager()

    def __unicode__(self):
        return self.name


class JournalEntry(models.Model):
    journal = models.ForeignKey(Journal, related_name='entries')
    headline = models.CharField(max_length=255)
    text = models.TextField(blank=True)
    location = models.CharField(max_length=255)
    datetime = models.DateTimeField(default=datetime.now())


    class Meta:
        verbose_name = "Journal entry"
        verbose_name_plural = "Journal entries"

    def __unicode__(self):
        return u'%s - %s' % (self.journal, self.headline)


class JournalPhoto(models.Model):
    entry = models.ForeignKey(JournalEntry, related_name='photos')
    image = FileBrowseField(max_length=200)
    highlight = models.BooleanField(default=False)
