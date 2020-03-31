A Simple Django Project Layout
===============================

:date: 2012-03-12 10:00
:modified: 2014-12-12 13:30
:slug: simply-django-project-layout
:tags: django,documentation,layout,projects,python,settings,simple
:lang: en

**UPDATE:** This article was originally written when Django version was 1.4. Since this article was published I made changes based on the new features of Django. You can see some of them in this repository: `https://github.com/jackboot7/django-project-template. <https://github.com/jackboot7/django-project-template>`_

This is short entry on how I organize my Django projects, in a way that will be easy to deploy to a production server. This is not meant to be a full tutorial on Django, but just to document the way I layout my Django applications. I consider this layout a work in progress, as each day I learn something new that I can integrate into my project's layout. Anyway, I hope someone else can find this entry useful.

For most of my small/pet/side projects, I use a simple server schema, working only with a local development machine and a production server, I know that is a good practice to use a staging server with the same setup as the production server, but for small projects I found this unnecessary.

Project Layout
++++++++++++++

First, let me show you the layout of most of my projects:

.. code-block:: bash

    | - project_domain_name/
    | | - .gitignore (.hgignore )
    | | - requirements.pip
    | | - env/                       # Virtual enviroment.
    | | - var/
    | | - server_config/             # Server configuration files.
    | | | - nginx.conf
    | | | - uwsgi.ini
    | | |
    | | - server_logs/               # Server logs.
    | | | - errors.log
    | | | - access.log
    | | |
    | | - project_dir/               # Django project. Most of the time I name it 'webapp'
    | | | - apps/                    # Application apps.
    | | | - templates/
    | | | - static/
    | | | - manage.py
    | | | - urls.py
    | | | - settings.py
    | | | - local_settings.py


Ignored files
+++++++++++++

Some of this files and dirs are meant to be ignored by the control version system.

***local_settings.py***, for every local development machine, there should be a local settings file, this is where you put all the local development settings such as database config, or additional apps such as south or django-extensions.

I use ***env/*** as a directory to install the virtual enviroment, in case you're using virtualenvwrapper you won't need to have this in your project directory.

***var/*** is a place to put everything related to the project in runtime, such as sqlite database files, or generated files from compass or coffeescript. Just like the local settings, this directory its supposed to be different for every local development machine.

Settings and Local Settings
+++++++++++++++++++++++++++

As you can see, I use two separate settings files, that way I can keep my production settings on my version control repository, and do daily work with the local settings of my development machine.

At the end of the settings.py file I import the local_settings module, in which I overwrite or add any specific setting that differ from the production one.

.. code-block:: python
    
    try:
        from local_settings import *
    except ImportError:
            pass

This way the deployment process is easier from the application's setup point of view.

Paths
------
The paths on my settings' file are defined using the os module. Even if this isn't the standard way to define paths, I find this useful as it makes easier to work with a project in different machines (local and production, more than one developer on the same project).


.. code-block:: python
    
    import os
    
    SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
    PROJECT_DIR = os.path.split(SITE_ROOT)[0]
    VAR_ROOT = os.path.join(PROJECT_DIR, 'var')
    
    if not os.path.exists(VAR_ROOT):
        os.mkdir(VAR_ROOT)

If we add this on the top of the setting file, we can later use these names to define standard variables such as ***TEMPLATE_DIRS*** or ***STATICFILES_DIR***, like this:

.. code-block:: python
    
    STATICFILES_DIRS = (os.path.join(SITE_ROOT, 'static'),)
    TEMPLATE_DIRS = (os.path.join(SITE_ROOT, 'templates'),)
                             

And so on with every absolute path that I have to define in my settings file.

This is a very simple layout for Django projects, but I've found that as simple as it is, it's still very powerful. In my github you can find a sample of this layout, feel free to fork it and improve it!

I always find interesting how other people have different standards and use different techniques to setup their own projects, that's why I really like to recommend Django Sites, which is a repository of django-based sites along with source code.

How do you layout your Django applications? Do you have any recommendation?
