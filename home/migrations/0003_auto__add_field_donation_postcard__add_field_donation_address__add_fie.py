# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Donation.postcard'
        db.add_column('home_donation', 'postcard', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'Donation.address'
        db.add_column('home_donation', 'address', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Donation.city'
        db.add_column('home_donation', 'city', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True), keep_default=False)

        # Adding field 'Donation.state'
        db.add_column('home_donation', 'state', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Donation.postcard'
        db.delete_column('home_donation', 'postcard')

        # Deleting field 'Donation.address'
        db.delete_column('home_donation', 'address')

        # Deleting field 'Donation.city'
        db.delete_column('home_donation', 'city')

        # Deleting field 'Donation.state'
        db.delete_column('home_donation', 'state')


    models = {
        'home.donation': {
            'Meta': {'ordering': "['date', 'last_name', 'first_name', 'amount']", 'object_name': 'Donation'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'cleared': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'postcard': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'received': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'})
        },
        'home.post': {
            'Meta': {'ordering': "['publish_date']", 'object_name': 'Post'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'publish_date': ('django.db.models.fields.DateField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['home']
