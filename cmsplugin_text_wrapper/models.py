# -*- coding: utf-8 -*-
from cms.plugins.text.models import AbstractText
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.html import strip_tags
from django.utils.text import Truncator
from fields import MultiSelectField


class TextWrapper(AbstractText):
    """
    Alternative text class with wrapper functionality
    """
    class Meta:
        db_table = 'cmsplugin_text'

    WRAPPERS = tuple((w[0], w[0]) for w in settings.CMS_TEXT_WRAPPERS)
    CLASSES = tuple((k, w) for k, w in enumerate(settings.CMS_TEXT_WRAPPER_CLASSES))
    wrapper = models.CharField(max_length=50, choices=WRAPPERS, blank=True, verbose_name=_('Wrap into'))
    classes = MultiSelectField(max_length=250, blank=True, null=True, choices=CLASSES,
                                verbose_name=_('Apply extra classes'))

    def __unicode__(self):
        if self.wrapper:
            text = Truncator(u'%s: %s' % (self.wrapper, strip_tags(self.body)))
        else:
            text = Truncator(strip_tags(self.body))
        return Truncator(text.words(7)).chars(38)
