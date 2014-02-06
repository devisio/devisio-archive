# encoding: utf8
from django.db import models, migrations
import filemanager.fields


class Migration(migrations.Migration):
    
    dependencies = [
        ('boxes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('box_ptr', models.OneToOneField(auto_created=True, primary_key=True, to_field='id', serialize=False, to='boxes.Box')),
                ('image', filemanager.fields.FilemanagerField(unique=True, max_length=255)),
            ],
            options={
                'verbose_name': 'Photo',
                'verbose_name_plural': 'Photos',
            },
            bases=('boxes.box',),
        ),
    ]
