# -*- coding: utf-8 -*-
from cms.plugins.text.models import AbstractText
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.html import strip_tags
from django.utils.text import Truncator


class TextWrapper(AbstractText):
    """
    Alternative text class with wrapper functionality
    """
    class Meta:
        db_table = 'cmsplugin_text'

    CHOICES = tuple((w[0], w[0]) for w in settings.CMS_TEXT_WRAPPERS)
    wrapper = models.CharField(max_length=50, choices=CHOICES, blank=True,
                               verbose_name=_('Wrap into'))

    def __unicode__(self):
        if self.wrapper:
            text = Truncator(u'%s: %s' % (self.wrapper, strip_tags(self.body)))
        else:
            text = Truncator(strip_tags(self.body))
        return Truncator(text.words(7)).chars(38)
