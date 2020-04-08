#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime


AUTHOR = u'Luis Alberto Santana'
AUTHOR_TAGLINE = u"Computer Scientist / Programmer."
SITELOGO = "https://2.gravatar.com/avatar/e426d5ca1f331cb8418614b7439a8dcd?v=2&s=150"
GRAVATAR_PERMALINK = "https://2.gravatar.com/avatar/e426d5ca1f331cb8418614b7439a8dcd?v=2&s=150"

ROBOTS = 'index, follow'

COPYRIGHT_YEAR = datetime.now().year

SITENAME = u'Luis Alberto Santana'
# SITEURL = 'https://www.jackboot7.com'

BROWSER_COLOR = '#FFF'
PYGMENTS_STYLE = 'solarized-light'

PATH = 'content'

STATIC_PATHS = ['images', 'files', 'extra/CNAME', 'birthday2014', 'extra/custom.css']

EXTRA_PATH_METADATA = {
     'extra/custom.css': {'path': 'extra/custom.css'},
     'extra/CNAME': {'path': './CNAME'},
    }

CUSTOM_CSS = 'extra/custom.css'

TIMEZONE = 'America/Caracas'

# Date Format and Locale
DEFAULT_LANG = u'en'
LOCALE = ('en_US')
DEFAULT_DATE_FORMAT = '%A, %b %d, %Y'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None


# Do not display the categories in the top bar
DISPLAY_CATEGORIES_ON_MENU = False

SITESUBTITLE = '@jackboot7'


SUMMARY_MAX_LENGTH = 300

# Theme
THEME = 'Flex'

# Menu
MAIN_MENU = True

# Enlaces
LINKS =  (
    ('Engineering Management Resources', 'https://www.jackboot7.com/engineering-management/'),
)

# Social widget
SOCIAL = (
    ('github', 'https://github.com/jackboot7'),
    ('twitter', 'https://twitter.com/jackboot7'),
    ('linkedin', 'https://www.linkedin.com/in/lsantanaf'),
    ('stack-overflow', 'https://stackoverflow.com/users/1170195/luis-alberto-santana'),
    ('rss', 'feeds/all.atom.xml'),
)

# MENUITEMS = (
#     ('Tags', '/tags.html'),
#     ('Archive', '/archives.html'),
# )

DEFAULT_PAGINATION = 5

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
