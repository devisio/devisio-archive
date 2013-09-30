# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'JournalEntry.headline'
        db.add_column(u'journals_journalentry', 'headline',
                      self.gf('django.db.models.fields.CharField')(default='Headline', max_length=255),
                      keep_default=False)

        # Adding field 'JournalEntry.text'
        db.add_column(u'journals_journalentry', 'text',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'JournalEntry.photos'
        db.add_column(u'journals_journalentry', 'photos',
                      self.gf('filebrowser.fields.FileBrowseField')(default='', max_length=200),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'JournalEntry.headline'
        db.delete_column(u'journals_journalentry', 'headline')

        # Deleting field 'JournalEntry.text'
        db.delete_column(u'journals_journalentry', 'text')

        # Deleting field 'JournalEntry.photos'
        db.delete_column(u'journals_journalentry', 'photos')


    models = {
        u'accounts.account': {
            'Meta': {'object_name': 'Account'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '50', 'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'journals.journal': {
            'Meta': {'object_name': 'Journal'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounts.Account']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        u'journals.journalentry': {
            'Meta': {'object_name': 'JournalEntry'},
            'datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 9, 30, 0, 0)'}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'journal': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['journals.Journal']"}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'photos': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200'}),
            'text': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['journals']