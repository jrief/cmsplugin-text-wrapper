# -*- coding: utf-8 -*-
import os
from django.conf import settings
from cms.plugin_pool import plugin_pool
from cms.plugins import text
from cms.plugins.text.utils import plugin_tags_to_user_html
from cms.plugins.text.cms_plugins import TextPlugin as TextPluginBase
from cmsplugin_text_wrapper.models import TextWrapper
from cmsplugin_text_wrapper.forms import TextForm


TEMPLATE_DIRS = getattr(settings, "TEMPLATE_DIRS", ()) + (os.path.join(os.path.dirname(text.__file__), 'templates'),)
setattr(settings, 'TEMPLATE_DIRS', TEMPLATE_DIRS)


class TextPlugin(TextPluginBase):
    model = TextWrapper
    form = TextForm

    def render(self, context, instance, placeholder):
        wrappers = [w[1] for w in settings.CMS_TEXT_WRAPPERS if w[0] == instance.wrapper]
        if wrappers:
            instance.render_template = wrappers[0].get('render_template')
            context.update(wrappers[0].get('extra_context', {}))
        extra_classes = []
        for csscls in instance.classes:
            try:
                extra_classes.append(dict(instance.CLASSES)[int(csscls)])
            except (ValueError, IndexError):
                pass
        context['extra_classes'] = ' '.join(extra_classes)
        context.update({
            'body': plugin_tags_to_user_html(instance.body, context, placeholder),
            'placeholder': placeholder,
            'object': instance,
        })
        return context

plugin_pool.unregister_plugin(TextPluginBase)
plugin_pool.register_plugin(TextPlugin)
