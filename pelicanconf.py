#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jacob Cook'
SITENAME = u'Jacob Cook'
AUTHOR_EMAIL = u'jacob@jcook.cc'
SITEURL = 'http://localhost:8000'

TIMEZONE = 'America/Montreal'
DEFAULT_DATE_FORMAT = ('%Y-%m-%d')

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
    ('Twitter', 'http://twitter.com/jcookcc'),
    ('GNU Social', 'https://micro.jcook.cc'),
    ('Github', 'http://github.com/jacook'),
    ('LinkedIn', 'http://ca.linkedin.com/pub/jacob-cook/17/138/5a5'),
    ('Last.fm', 'http://last.fm/user/midnight1617'),
    ('Email', 'mailto:jacob@jcook.cc'),
    ('RSS', '/feed'),
)

DEFAULT_PAGINATION = 10

# Content path.
PATH = 'content'
PAGE_DIR = 'pages'
ARTICLE_DIR = 'posts'

# URL settings
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)
ARTICLE_URL = ('{category}/{slug}/')
ARTICLE_SAVE_AS = ('{category}/{slug}/index.html')
PAGE_URL = ('pages/{slug}/')
PAGE_SAVE_AS = ('pages/{slug}/index.html')
PAGE_LANG_SAVE_AS = False
TAG_URL = ('tag/{slug}/')
TAG_SAVE_AS = ('tag/{slug}/index.html')
TAGS_URL = ('tags/')
TAGS_SAVE_AS = None
CATEGORY_URL = ('category/{slug}/')
CATEGORY_SAVE_AS = ('category/{slug}/index.html')
AUTHOR_SAVE_AS = False

# Feed
#FEED_DOMAIN = SITEURL
#FEED_ALL_ATOM = 'feeds/all.atom.xml'
#CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
#TRANSLATION_FEED_ATOM = None

# Theme
THEME = 'theme'
AVATAR_URL = '/images/avatar.jpg'
COVER_IMG_URL = '/images/cover.jpg'
TYPOGRIFY = True
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
