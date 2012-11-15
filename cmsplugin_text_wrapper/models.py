# -*- coding: utf-8 -*-
from cms.plugins.text.models import AbstractText
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Text(AbstractText):
    """
    Alternative text class with wrapper functionality
    """
    class Meta:
        app_label = 'cms_plugins_text'

#    CHOICES = tuple((w[0], w[0]) for w in settings.CMS_TEXT_WRAPPERS)
#    wrapper = models.CharField(max_length=50, choices=CHOICES, blank=True,
#                               verbose_name=_('Wrap into'))
