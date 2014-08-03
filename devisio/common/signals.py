import os

from PIL import Image

from django.conf import settings
from django.dispatch import receiver

from filemanager.core import Filemanager
from filemanager.settings import MEDIA_ROOT as FILEMANAGER_MEDIA_ROOT
from filemanager.signals import filemanager_post_upload


@receiver(filemanager_post_upload, sender=Filemanager)
def photo_processor(sender, filename, path, filepath, **kwargs):
    name, extension = filename.split('.')

    if not extension in ['jpg', 'jpeg']:
        return # not photo, nothing to do here

    thumbnail_path = os.path.join(settings.MEDIA_THUMBNAILS_ROOT, path)

    # create directory
    if not os.path.exists(thumbnail_path):
        os.makedirs(thumbnail_path)

    image = Image.open(os.path.join(FILEMANAGER_MEDIA_ROOT, filepath))

    print(image.size[0], image.size[1])

    LONG_EDGE = 1600

    if image.size[0] > image.size[1]:
        ratio = image.size[1] / image.size[0]
        dimensions = (LONG_EDGE, int(LONG_EDGE*ratio))
    else:
        ratio = image.size[0] / image.size[1]
        dimensions = (int(LONG_EDGE*ratio), LONG_EDGE)

    print(dimensions)

    thumbnail = image.resize(dimensions, Image.ANTIALIAS)
    thumbnail.save(os.path.join(thumbnail_path, filename), 'jpeg')

    journal_filename = '%s-%s.%s' % (name, 'journal', extension)

    JOURNAL_EDGE_LENGTH = 400
    m = min(image.size[0]/JOURNAL_EDGE_LENGTH, image.size[1]/JOURNAL_EDGE_LENGTH)
    d = (int(image.size[0]/m), int(image.size[1]/m))
    print(d)
    thumbnail = image.resize(d, Image.ANTIALIAS)
    b = (int((d[0]-JOURNAL_EDGE_LENGTH)/2), int((d[1]-JOURNAL_EDGE_LENGTH)/2), int((d[0]-JOURNAL_EDGE_LENGTH)/2)+JOURNAL_EDGE_LENGTH, int((d[1]-JOURNAL_EDGE_LENGTH)/2)+JOURNAL_EDGE_LENGTH)
    print(b)
    thumbnail = thumbnail.crop(b)
    thumbnail.save(os.path.join(thumbnail_path, journal_filename), 'jpeg')

    print(sender, filepath, path, filename)
