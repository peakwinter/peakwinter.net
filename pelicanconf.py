#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jacob Cook'
SITENAME = u'Jacob Cook'
AUTHOR_EMAIL = u'jacob@jcook.cc'
SITEURL = 'https://peakwinter.net'
#SITEURL = 'http://localhost:8000'

TIMEZONE = 'America/Montreal'
DEFAULT_DATE_FORMAT = ('%d %B %Y')

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DEFAULT_PAGINATION = 10

# Content path.
PATH = 'content'
PAGE_DIR = 'pages'
ARTICLE_DIR = 'articles'

# URL settings
PAGINATION_PATTERNS = (
    (1, '{base_name}/blog/', '{base_name}/blog/index.html'),
    (2, '{base_name}/blog/page/{number}/', '{base_name}/blog/page/{number}/index.html'),
)
TEMPLATE_PAGES = {'home.html': 'index.html'}
ARTICLE_URL = ('blog/{date:%Y}/{slug}/')
ARTICLE_SAVE_AS = ('blog/{date:%Y}/{slug}/index.html')
PAGE_URL = ('{slug}/')
PAGE_SAVE_AS = ('{slug}/index.html')
PAGE_LANG_SAVE_AS = False
TAG_URL = ('blog/tag/{slug}/blog/')
TAG_SAVE_AS = ('blog/tag/{slug}/index.html')
TAGS_URL = ('tags/')
TAGS_SAVE_AS = None
CATEGORY_SAVE_AS = False
AUTHOR_SAVE_AS = False
AUTHORS_SAVE_AS = False
ARCHIVES_SAVE_AS = False
CATEGORIES_SAVE_AS = False

# Feed
#FEED_DOMAIN = SITEURL
#FEED_ALL_ATOM = 'feeds/all.atom.xml'
#CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
#TRANSLATION_FEED_ATOM = None

# Theme
THEME = 'theme'
DEFAULT_PAGINATION = 10

# Plugin
PLUGIN_PATH = 'plugins'
PLUGINS = ['sitemap', 'gravatar', 'pelican_youtube']
PYGMENTS_RST_OPTIONS = {'cssclass': 'codehilite', 'linenos': 'table'}

# Sitemap.
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 1,
        'pages': 0.9,
        'indexes': 0.8,
    },
    'changefreqs': {
        'indexes': 'daily',
        'articles': 'daily',
        'pages': 'weekly'
    }
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
