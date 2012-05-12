# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Section'
        db.create_table('home_section', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=6, db_index=True)),
        ))
        db.send_create_signal('home', ['Section'])

        # Adding field 'Donation.card_name'
        db.add_column('home_donation', 'card_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding M2M table for field sections on 'Donation'
        db.create_table('home_donation_sections', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('donation', models.ForeignKey(orm['home.donation'], null=False)),
            ('section', models.ForeignKey(orm['home.section'], null=False))
        ))
        db.create_unique('home_donation_sections', ['donation_id', 'section_id'])


    def backwards(self, orm):
        
        # Deleting model 'Section'
        db.delete_table('home_section')

        # Deleting field 'Donation.card_name'
        db.delete_column('home_donation', 'card_name')

        # Removing M2M table for field sections on 'Donation'
        db.delete_table('home_donation_sections')


    models = {
        'home.donation': {
            'Meta': {'ordering': "['date', 'last_name', 'first_name', 'amount']", 'object_name': 'Donation'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'card_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'cleared': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
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
