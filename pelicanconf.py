#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


AUTHOR = u'Luis Alberto Santana'
AUTHOR_TAGLINE = u"Computer Scientist / Programmer."
GRAVATAR_PERMALINK = "https://2.gravatar.com/avatar/e426d5ca1f331cb8418614b7439a8dcd?v=2&s=150"

SITENAME = u'Luis Alberto Santana'
#SITEURL = 'www.jackboot7.com'

PATH = 'content'

TIMEZONE = 'America/Caracas'

# Date Format and Locale
DEFAULT_LANG = u'en'
LOCALE = ('en_US')
DEFAULT_DATE_FORMAT = '%A, %b %d, %Y'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Do not display the categories in the top bar
DISPLAY_CATEGORIES_ON_MENU = False

SITESUBTITLE = '@jackboot7'


SUMMARY_MAX_LENGTH = 400

# Theme
THEME = 'clean-blog'

# Enlaces
# LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
    ('Github', 'https://github.com/jackboot7'),
    ('Twitter', 'https://twitter.com/jackboot7'),
    ('Linkedin', 'https://www.linkedin.com/in/lsantanaf'),
    ('StackOverflow', 'https://stackoverflow.com/users/1170195/luis-alberto-santana'),
    ('Last.fm', 'https://last.fm/user/jackboot7'),
    ('Delicious', 'https://delicious.com/jackboot7'),
    ('Carers SO', 'https://careers.stackoverflow.com/jackboot7'),
)


DEFAULT_PAGINATION = 15
STATIC_PATHS = ['images', 'files', 'extra/CNAME', 'birthday2014']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': './CNAME'}, } 
READERS = {"html": None}

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Tag Cloud
TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 100

# Twitter Username
TWITTER_USERNAME = 'jackboot7'

# Disqus

# Line numbers in every code block
PYGMENTS_RST_OPTIONS = {'classprefix': 'pgcss', 'linenos': 'table'}


# ====================================
#  Settings for Pelican Clean Blog
# ====================================

GITHUB_URL = 'https://github.com/jackboot7'
TWITTER_URL = 'https://twitter.com/jackboot7'
FACEBOOK_URL = '#'

COLOR_SCHEME_CSS = 'monokai.css'
