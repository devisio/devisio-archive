from django.conf import settings
from django.db import models


class Journal(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    location = models.CharField(max_length=255)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False)

    def __unicode__(self):
        return self.name


class JournalEntry(models.Model):
    journal = models.ForeignKey(Journal)
    location = models.CharField(max_length=255)
    datetime = models.DateTimeField()

    class Meta:
        verbose_name = "Journal entry"
        verbose_name_plural = "Journal entries"
