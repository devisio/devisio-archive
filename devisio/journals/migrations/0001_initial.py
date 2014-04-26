# encoding: utf8
from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=255)),
                ('subtitle', models.CharField(max_length=255)),
                ('headline', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('slug', models.SlugField()),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('published_at', models.DateTimeField(default=datetime.datetime(2014, 4, 17, 13, 44, 26, 863181))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
