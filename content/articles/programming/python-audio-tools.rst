Python Audio Tools
===================

:date: 2012-02-15 11:04
:modified: 2014-12-12 13:30
:slug: python-audio-tools
:tags: api, audio,audiotools,code,conversion,convert,encoding,example,flac,lame,m4a,mp3,programming,python
:lang: en

Some days ago, I started to work on a web application that requires to encode audio wave files (.wav) into three other formats, being: MP3, Flac and M4A. That encoding will run in its own Celery task.

One thing I knew for certain is that I wouldn't be running commands such as lame or flac directly.

Since the project is being written in Python, I though it would be nice to use a library to do all the encoding directly in Python code, without calling any external program..

If you're going to write an audio related application in Python, I recommend a visit to the `audio section <http://wiki.python.org/moin/Audio>`_ in the Python wiki, where you can find all the audio related modules that are available for Python.

I decided to use the API from `Python Audio Tools <http://audiotools.sourceforge.net/>`_, which is a very complete library to do audio manipulation. In the backend, it uses lame, flac and other commands to do the enconding of the files, but I won't have to run those commands directly.

So far, I'm very happy with the results I've got using audiotools, since it deals with metadata for the audio files (ID3v2 tagging, et al.) and it can even embed artwork into the files (if the format support such metadata).

I wrote a small Python script to show a basic use of this library, if you want, you can check it out on `my githhub repo <https://github.com/jackboot7/python-audiotools-test>`_. I'll be adding a little more functionality to it as soon as I got some free time.
