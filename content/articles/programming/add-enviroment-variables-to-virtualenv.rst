Quick tip: Adding Variables to env in a Virtualenv (for development purpose)
=============================================================================

:date: 2015-07-16 13:40
:slug: virtualenv-add-vars-to-env
:tags: python, enviroment, virtualenv, export, bash
:lang: en


If you're working with third party APIs, you might find code like `YOUR_SECRET_KEY="some secret api key"` in your source code, this is a bad practices for a lot of reasons (security, source code sharing, etc). Instead, the recommended way to manage this kind of situation is to add the value as a enviroment variable, and read it in your code with something like this:

.. code:: python

    import os
    os.environ.get('YOUR_SECRET_KEY')

So, how do you avoid to add the variable to the enviroment each time you do some coding? If you're working with virtualenv you simply add it in the `env/bin/activate` script:


.. code:: bash


    YOUR_SECRET_KEY="some secret api key"
    export YOUR_SECRET_KEY

