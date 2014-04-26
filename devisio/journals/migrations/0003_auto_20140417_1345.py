# encoding: utf8
from django.db import models, migrations
import datetime
import filemanager.fields


class Migration(migrations.Migration):

    dependencies = [
        ('journals', '0002_journalsection'),
    ]

    operations = [
        migrations.AddField(
            model_name='journal',
            name='photo',
            field=filemanager.fields.FilemanagerField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='journal',
            name='published_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 4, 17, 13, 44, 56, 741657)),
        ),
    ]
