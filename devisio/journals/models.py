from datetime import datetime

from django.conf import settings
from django.db import models

from filemanager.fields import FilemanagerField


""" The journal itself is its first section. """
class Journal(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    photo = FilemanagerField(max_length=255)
    headline = models.CharField(max_length=255)
    text = models.TextField()
    slug = models.SlugField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.title


class JournalSection(models.Model):
    journal = models.ForeignKey(Journal, related_name='sections')
    position = models.PositiveIntegerField()
    headline = models.CharField(max_length=255)
    slug = models.SlugField()
    text = models.TextField()

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ('position',)
