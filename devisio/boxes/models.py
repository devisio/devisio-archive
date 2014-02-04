from django.db import models


class Box(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True, default='')

    def __str__(self):
        return self.title
