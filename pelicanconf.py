#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Josh Walawender'
SITENAME = "Twilight Landscapes Blog"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'US/Hawaii'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('My Photography', 'https://twilightlandscapes.com'),
         )

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

HEADER_COVER = 'images/6D-7894.jpg'
GITHUB_URL = 'http://github.com/joshwalawender'

# STATIC_PATHS = 'content/pages/IRAFtutorial'

# Notes
# pelican content -o output -s pelicanconf.py -t pelican-clean-blog -r --listen
# ghp-import -m "Generate Pelican site" --no-jekyll -b master output
