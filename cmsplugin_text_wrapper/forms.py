# -*- coding: utf-8 -*-
from cmsplugin_text_wrapper.models import TextWrapper
from django import forms
from django.forms.models import ModelForm


class TextForm(ModelForm):
    body = forms.CharField()

    class Meta:
        model = TextWrapper
        fields = ('wrapper', 'body')
        exclude = ('page', 'position', 'placeholder', 'language', 'plugin_type')
