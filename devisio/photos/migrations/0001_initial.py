# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Album'
        db.create_table(u'photos_album', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.Account'])),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 5, 25, 0, 0))),
            ('visible', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'photos', ['Album'])

        # Adding model 'Photo'
        db.create_table(u'photos_photo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('album', self.gf('django.db.models.fields.related.ForeignKey')(related_name='photos', to=orm['photos.Album'])),
            ('image', self.gf('filebrowser.fields.FileBrowseField')(max_length=200)),
        ))
        db.send_create_signal(u'photos', ['Photo'])


    def backwards(self, orm):
        # Deleting model 'Album'
        db.delete_table(u'photos_album')

        # Deleting model 'Photo'
        db.delete_table(u'photos_photo')


    models = {
        u'accounts.account': {
            'Meta': {'object_name': 'Account'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'photos.album': {
            'Meta': {'ordering': "['-date']", 'object_name': 'Album'},
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 5, 25, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.Account']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'photos.photo': {
            'Meta': {'object_name': 'Photo'},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'photos'", 'to': u"orm['photos.Album']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['photos']