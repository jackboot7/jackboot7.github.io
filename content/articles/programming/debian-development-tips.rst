Debian (development tips)
=========================

:date: 2014-12-13 11:58
:modified: 2015-10-29 16:38
:slug: debian-development-tips
:tags: debian,help,documentation,libraries,pil,libjpeg,locale,matplotlib,libxml,ubuntu,freetype,postgresql,database,scipy
:lang: en       

These are some extra steps that I've found necessary when starting development in a recently-installed Debian machine.


Jpeg support in PIL and pillow.
+++++++++++++++++++++++++++++++

.. code:: bash

    $ sudo apt-get install libjpeg libjpeg-dev libfreetype6 libfreetype6-dev zlib1g-dev
    $ sudo ln -s /usr/lib/`uname -i`-linux-gnu/libfreetype.so /usr/lib/
    $ sudo ln -s /usr/lib/`uname -i`-linux-gnu/libjpeg.so /usr/lib/
    $ sudo ln -s /usr/lib/`uname -i`-linux-gnu/libz.so /usr/lib/


Installing lxml in Python (Debian  based).
++++++++++++++++++++++++++++++++++++++++++

If you're getting the **"fatal error: libxml/xmlversion.h: No such file or directory"** error, just install the following development files:

.. code:: bash

    $ sudo apt-get install python-dev libxml2-dev libxslt1-dev 


Problems with 'matplotlib' and freetype.
+++++++++++++++++++++++++++++++++++++++++

If you're having problems installing matplotlib in a Python virtualenv, and are getting the *'freetype missing'* error, you sould install the development files for freetype, and (in most cases) rebuild the python dependencies for matplotlib.

.. code:: bash
    
    $ sudo apt-get  -u install libfreetype6-dev
    $ sudo apt-get build-dep python-matplotlib

After that, you can just use pip normally to install matplotlib

.. code:: bash
    
    $ pip install matplotlib

PS. I know of cases where you have to update *python-virtualenv* and *python-pip* after you use build-dep. Just apt-get upgrade your installation.
Today I learned about the 'pydoc' command from Python.


Problems with locale
++++++++++++++++++++

In some machines I've found problems when setting locales from Python.  First check the results of running 

.. code:: bash

    $ locale

In my case is:

.. code:: bash

    LANG=es_VE.UTF-8
    LANGUAGE=es_VE:es
    LC_CTYPE="es_VE.UTF-8"
    LC_NUMERIC="es_VE.UTF-8"
    LC_TIME="es_VE.UTF-8"
    LC_COLLATE="es_VE.UTF-8"
    LC_MONETARY="es_VE.UTF-8"
    LC_MESSAGES="es_VE.UTF-8"
    LC_PAPER="es_VE.UTF-8"
    LC_NAME="es_VE.UTF-8"
    LC_ADDRESS="es_VE.UTF-8"
    LC_TELEPHONE="es_VE.UTF-8"
    LC_MEASUREMENT="es_VE.UTF-8"
    LC_IDENTIFICATION="es_VE.UTF-8"
    LC_ALL=


Then use:

.. code:: py
    
    import locale

    try:
        locale.setlocale(locale.LC_ALL, 'es_VE.utf-8')
    except locale.Error:
        raise


Change es_VE.UTF-8 for yours.


Creating postgresql roles
++++++++++++++++++++++++++

This one is not just for Debian based systems, but for PostgreSQL, giving privileges to a specific user in your Database Server is really simple:

.. code:: bash
    
    CREATE USER user_name WITH PASSWORD 'userpasswd';
    
    CREATE DATABASE new_database;

    GRANT ALL PRIVILEGES ON DATABASE new_database to user_name;


Local dependencies for scipy
++++++++++++++++++++++++++++

Before you're able to build `scipy` using `pip install`, you'll need to have some dependencies installed.


.. code:: bash
    
    $ sudo apt-get -u install libatlas-base-dev libatlas-dev liblapack-dev libblas-dev

You'll also need a Fortran compiler installed.

.. code:: bash
    
    $ sudo apt-get -u install gfortran
