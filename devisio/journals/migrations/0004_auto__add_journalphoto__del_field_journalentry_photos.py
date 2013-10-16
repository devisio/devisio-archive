# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'JournalPhoto'
        db.create_table(u'journals_journalphoto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('entry', self.gf('django.db.models.fields.related.ForeignKey')(related_name='photos', to=orm['journals.JournalEntry'])),
            ('image', self.gf('filebrowser.fields.FileBrowseField')(max_length=200)),
            ('highlight', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'journals', ['JournalPhoto'])

        # Deleting field 'JournalEntry.photos'
        db.delete_column(u'journals_journalentry', 'photos')


    def backwards(self, orm):
        # Deleting model 'JournalPhoto'
        db.delete_table(u'journals_journalphoto')


        # User chose to not deal with backwards NULL issues for 'JournalEntry.photos'
        raise RuntimeError("Cannot reverse this migration. 'JournalEntry.photos' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'JournalEntry.photos'
        db.add_column(u'journals_journalentry', 'photos',
                      self.gf('filebrowser.fields.FileBrowseField')(max_length=200),
                      keep_default=False)


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
            'datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 10, 16, 0, 0)'}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'journal': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entries'", 'to': u"orm['journals.Journal']"}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'text': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'journals.journalphoto': {
            'Meta': {'object_name': 'JournalPhoto'},
            'entry': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'photos'", 'to': u"orm['journals.JournalEntry']"}),
            'highlight': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['journals']