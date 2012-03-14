# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Donation.full_name'
        db.delete_column('home_donation', 'full_name')

        # Deleting field 'Donation.common_name'
        db.delete_column('home_donation', 'common_name')

        # Adding field 'Donation.first_name'
        db.add_column('home_donation', 'first_name', self.gf('django.db.models.fields.CharField')(default='', max_length=50), keep_default=False)

        # Adding field 'Donation.last_name'
        db.add_column('home_donation', 'last_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # User chose to not deal with backwards NULL issues for 'Donation.full_name'
        raise RuntimeError("Cannot reverse this migration. 'Donation.full_name' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Donation.common_name'
        raise RuntimeError("Cannot reverse this migration. 'Donation.common_name' and its values cannot be restored.")

        # Deleting field 'Donation.first_name'
        db.delete_column('home_donation', 'first_name')

        # Deleting field 'Donation.last_name'
        db.delete_column('home_donation', 'last_name')


    models = {
        'home.donation': {
            'Meta': {'ordering': "['date', 'last_name', 'first_name', 'amount']", 'object_name': 'Donation'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'cleared': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'received': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
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
