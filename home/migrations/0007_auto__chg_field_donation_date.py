# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Donation.date'
        db.alter_column('home_donation', 'date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))


    def backwards(self, orm):
        
        # Changing field 'Donation.date'
        db.alter_column('home_donation', 'date', self.gf('django.db.models.fields.DateField')(auto_now_add=True))


    models = {
        'home.donation': {
            'Meta': {'ordering': "['date', 'last_name', 'first_name', 'amount']", 'object_name': 'Donation'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'card_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'cleared': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'payment_type': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'postcard': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'received': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sections': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'donations'", 'symmetrical': 'False', 'to': "orm['home.Section']"}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'})
        },
        'home.post': {
            'Meta': {'ordering': "['publish_date']", 'object_name': 'Post'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'publish_date': ('django.db.models.fields.DateField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'home.section': {
            'Meta': {'object_name': 'Section'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '6', 'db_index': 'True'})
        }
    }

    complete_apps = ['home']
