from django.db import models
from django.utils.translation import ugettext_lazy as _


class Box(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True, default='')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Box")
        verbose_name_plural = _("Boxes")
