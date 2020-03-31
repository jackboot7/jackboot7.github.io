(Local) Online Python Documentation
===================================

:date: 2010-10-15 11:38
:modified: 2015-12-09 11:12
:slug: pydoc
:tags: python, help, documentation
:lang: en


Today I learned about the `pydoc` command from Python. Even if you're offline you can access the standard library documentation running from a local copy using the command mentioned above.

Simply introduce this command in your terminal:



.. code-block:: bash
    
    $ pydoc -p 8000

Then you can go to `http://locahost:8000 <http://localhost:8000>`_. This way you can browse the documentation for all your installed Python modules in the same way you'd use the 'help' command from the Python CLI.

[1] `http://docs.python.org/library/pydoc.html <http://docs.python.org/library/pydoc.html>`_

[2] `http://pydoc.org/ <http://pydoc.org/>`_


