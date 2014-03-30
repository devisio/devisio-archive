from django.db import models


class Journal(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
