# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        db.add_column('cmsplugin_text', 'wrapper',
              self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True),
              keep_default=False)

    def backwards(self, orm):
        db.delete_column('cmsplugin_text', 'wrapper')

    models = {
        
    }

    complete_apps = ['cmsplugin_text_wrapper']