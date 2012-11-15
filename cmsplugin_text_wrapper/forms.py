# -*- coding: utf-8 -*-
from cmsplugin_text_wrapper.models import Text
from django import forms
from django.forms.models import ModelForm


class TextForm(ModelForm):
    body = forms.CharField()

    class Meta:
        model = Text
        fields = ('wrapper', 'body')
        exclude = ('page', 'position', 'placeholder', 'language', 'plugin_type')
