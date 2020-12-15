#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Josh Walawender'
SITENAME = "Twilight Landscapes Blog"
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['images', 'IRAFtutorial']
ARTICLE_EXCLUDES = ['IRAFtutorial']

TIMEZONE = 'US/Hawaii'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

HEADER_COVER = 'images/IMG_5112.jpg'
GITHUB_URL = 'http://github.com/joshwalawender'

PATH = 'content'
STATIC_PATHS = ['static', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}}

INTRO_CONTENT = """Welcome to Josh Walawender's blog.  This mostly contains posts 
related to amateur astronomy such as observing reports.  You can check out some 
of my photography over at
<a href='https://www.twilightlandscapes.com'>www.twilightlandscapes.com</a>"""

# How to Publish:
# Local Test:
#   pelican content -o output -s pelicanconf.py -t pelican-clean-blog -r --listen
# Publish to GitHub:
#   pelican content -o output -s pelicanconf.py -t pelican-clean-blog
#   ghp-import -m "Generate Pelican site" --no-jekyll -b master output
#   git push origin master
