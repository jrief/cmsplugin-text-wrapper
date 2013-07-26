cmsplugin-text-wrapper
======================

A Django CMS plugin which extends and replaces the shipped text plugin with
simple wrapper functionalities.

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

and remove ``'cms.plugins.text'`` from ``INSTALLED_APPS`` if configured.

Then run ``manage.py migrate cmsplugin_text_wrapper`` to update your database
table ``cmsplugin_text``. This adds a column named ``wrapper`` and keeps
everything caompatible.

In case you set up a new instance of DjangoCMS, the migration scripts will
look for a table named ``cmsplugin_text`` and if it does not exists, create
it.

Restart your application. You may use all your text fields in exactly as before.
They then are marked for not using any wrapper and are rendered as before.

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

``extra_context`` is an optional dictionary containing any kind of data. The
context used to render the template is populated with this extra context.

This plugin does not change the admin interface, except for a pull down box on
top of the text editor. Using the default value is perfectly legal, in this case
the text wrapper plugin behaves exactly as the default text plugin as shipped
with **django-cms**.


The 960 pixel grid system 
-------------------------
One of the most widespread grid system is named http://960.gs/
This plugin interacts nicely with this grid system, but does not depend on it. This documentation
shows how to integrate this plugin with the 960.gs, but it might also work perfectly well with
Twitter Bootstrap.

The problem with the shipped text plugin is that an editor can add text, images, etc. to a
placeholder, but he gains no control over the layout of the given container. Often this is desired
behavior to enforce a consistent layout, but sometimes it is annoying, since too many specialized
templates have to be created.

Say, an editor wants to use the 960 Grid System with 12 columns. Now for for each possible
combinations of rows and colums, a special template must be created. This can result in a template
such as::

    <div class="container_12">
        <div class="grid_9">{% placeholder "g1" %}</div><div class="grid_3">{% placeholder "g2" %}</div>
        <div class="grid_6">{% placeholder "g3" %}</div><div class="grid_6">{% placeholder "g4" %}</div>
        <div class="grid_4">{% placeholder "g5" %}</div><div class="grid_4">{% placeholder "g6" %}</div><div class="grid_4">{% placeholder "g7" %}</div>
    </div>

Here each grid-div gets its own placeholder. If an editor needs many similar layouts such as the one
shown above, it can be hard to maintain all possible combinations of rows and columns.

This **cmsplugin-text-wrapper** gives an editor of a CMS page a flexible and clean way to add as
many different rows, with as many different columns as he wishes. Each of these columns can have
their own widths.

If this grid system is enforced, the editor gains control over certain parts of the layout without
having to fiddle with div tags nor snippets.

Download the files ``reset.css``, ``text.css`` and ``960.css`` from http://github.com/nathansmith/960-Grid-System/zipball/master
and add them to your stylesheets.

In your templates directory, create a template named ``container-12.html``::

    ... other stuff goes here
    <div class="container_12">
        {% placeholder "Container Content" %}
    </div>
    ... more stuff goes here

and add it to your CMS_TEMPLATES tuple.

In your templates directory, create another template named ``grid.html``::

    <div class="{{ grid_class }} {{extra_classes}}">
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
    CMS_TEXT_WRAPPER_CLASSES = ('alpha', 'omega',)

Now, after choosing a plugin of type **Text** in the CMS admin backend, two additionals fields are
added. The first is a select box labeled **Wrap into** where the editor can choose one of the
grids. The second is a list of checkboxes, one for each wrapper classes.


Version history
---------------
* 0.5: final release which could replace **cmsplugin-text** seamlessly.
* 0.6: added a MultipleSelectField to add extra classes to the wrapper.


Related plugins which works in a similar way as **cmsplugin-text-wrapper**:
...........................................................................


text-plugin-ng
--------------
Download from https://github.com/KristianOellegaard/cmsplugin-text-ng .

**text-plugin-ng** is not intended to replace the default text plugin. It is
an add on to the text plugin as shipped with Django CMS and is not compatible
with it. Therefore an editor gets a choice of two text plugin, the one shipped
with Django CMS and **cmsplugin-text-ng**. For each placeholder he then has to
choose from one of those two.

Additionally the editor has to maintain two extra tables with named templates.

django-cms-columns
------------------
Download from https://github.com/philomat/django-cms-columns

**django-cms-columns** offers support for the grid systems [YAML](http://www.yaml.de/en/documentation/practice/subtemplates.html) 
and [Blueprint](http://www.blueprintcss.org/) in the form of built in templates.

It does not seem to be supported any more.

