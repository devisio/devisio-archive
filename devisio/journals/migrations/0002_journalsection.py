# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JournalSection',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('journal', models.ForeignKey(to='journals.Journal', to_field='id')),
                ('position', models.PositiveIntegerField()),
                ('headline', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('text', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
