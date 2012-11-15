cmsplugin-text-wrapper
======================

A cms plugin which extends and replaces the text plugin shipped with django-cms
with simple wrapper functionalities.

Description
-----------

This plugin adds a simple wrapping functionality to the text plugin shipped with
django-cms. By adding this plugin, an editor may optionally choose a predefined
wrapper, which is rendered as template around the current content. This is
especially useful when working with predefined grids such as http://960.gs

This plugin is fully compatible with the default text plugin and offers all of
the current functionality. It shall therefore be used to replace the default
text plugin. It works together with both, the WYEditor as well as with the 
TinyMCE editor.

Dependencies
------------

* Django >= 1.3
* django-cms >= 2.3
* South >= 0.7

Installation
------------

add the plugin to ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...
        'cmsplugin_text_wrapper',  # alternative to 'cms.plugins.text'
        ...
    )

and remove 'cms.plugins.text' from ``INSTALLED_APPS`` if configured.

Then run ``manage.py migrate cmsplugin_text_wrapper`` to update your database
table ``cmsplugin_text``.

Restart your application. You may use all your text fields as before. They are
all marked for not using any wrapper.

Usage
-----

In your ``settings.py`` add a tuple of tuples such as::

	CMS_TEXT_WRAPPERS = (
	    ('<wrapper name>', {
	        'render_template': '<template name>',
	        'extra_context': <a dictionary with extra context to render the template>
	    }),
	    ...
	)

``<wrapper name>`` is a unique name to identify the wrapper. The second part of
each wrappers tuple contains a directory with the following keys:

``render_template`` is the name of the template to be used when rendering the
content of this text plugin. This template can contain some optional html
tags but must contain the following template variable::

	{{ body|safe }}

which is replaced by the editors content.

If ``render_template`` is missing, the content of this text plugin is rendered
in the same way, as the default text plugin renders its content.

``extra_context`` is an optional directory containing any kind of data. The
context used to render the template is populated with this extra context.

This plugin does not change the admin interface, except for a pull down box on
top of the text editor. Using the default value is perfectly legal, in this case
the text wrapper plugin behaves exactly as the default text plugin as shipped
with **django-cms**.


The 960 pixel grid system 
-------------------------

One of the most widespread grid system is named http://960.gs . This plugin
interacts nicely with this grid, but does not depend on it.

The problem with the shipped text plugin is that an editor can add text, images,
etc. to a placeholder, but he gains no control over the layout of the given
container. Often this is desired behavior but sometimes it is annoying.

So, if an editor wants to use the 960 Grid System with say 12 columns, a
template must be created for each possible combinations of rows. This can result
in templates such as::

    <begin container------------12>
      <grid-------------9> <grid-3>
      <grid-------6> <grid-------6>
      <grid--4> <grid--4> <grid--4>
    <end container---------------->

It can be hard to maintain all possible combinations of rows and columns.

This **rendering ** gives an editor of a CMS page a flexible and clean way to
add many different rows, each with a variable amount of columns and widths.

If this grid system is enforced, the editor gains control over certain parts of
the layout without having to fiddle with div tags or snippets.

Download the files ``960.css`` and ```reset.css`` and add them to your
stylesheets.

In your templates directory, create a template named ``container-12.html``::

    ... other stuff goes here
    <div class="container_12">
        {% placeholder "Container Content" %}
    </div>
    ... more stuff goes here

and add it to your CMS_TEMPLATES tuple.

In your templates directory, create another template named ``grid.html``::

    <div class="{{grid_class}}">
        {{ body|safe }}
    </div>

and add it in different configurations to your ``CMS_TEXT_WRAPPERS`` tuples::

    CMS_TEXT_WRAPPERS = (
        ('Grid 3', {
            'render_template': 'grid.html',
            'extra_context': {'grid_class': 'grid_3'}
        }),
        ('Grid 6', {
            'render_template': 'grid.html',
            'extra_context': {'grid_class': 'grid_6'}
        }),
        ('Grid 12', {
            'render_template': 'grid.html',
            'extra_context': {'grid_class': 'grid_12'}
        }),
        ... and more ...
    )


text-plugin-ng
--------------
There is another plugin which works similar to this one: https://github.com/KristianOellegaard/cmsplugin-text-ng .
The **text-plugin-ng** is not intended to replace the default text plugin. Is is
intended to be an additional plugin to the built-in text plugin. It also is not
compatible with the current text plugin and additional tables have to
maintained. It thus is not as simple to use as **cmsplugin-text-wrapper**.
