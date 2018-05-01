#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Site Author'
SITENAME = 'Site Name'
SITEURL = ''
THEME = 'themes/bootstrap-basic'

PATH = 'content'
STATIC_PATHS = ['images']
OUTPUT_PATH = 'build/'
DELETE_OUTPUT_DIRECTORY = True

DISPLAY_BREADCRUMBS = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True

TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# This puts a index.html file in a directory for each blog post but links only
# to the directory
ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
PAGE_LANG_URL = '{lang}/{slug}/'
PAGE_LANG_SAVE_AS = '{lang}/{slug}/index.html'
CATEGORY_URL = '{slug}/'
CATEGORY_SAVE_AS = '{slug}/index.html'
TAG_URL = '{slug}/'
TAG_SAVE_AS = '{slug}/index.html'
AUTHOR_URL = '{slug}/'
AUTHOR_SAVE_AS = '{slug}/index.html'
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

SLUGIFY_SOURCE = 'title'

SUMMARY_MAX_LENGTH = 10

MARKDOWN = {
    'extension_configs': {
        # Commenting out this next line turns off pygments
        # 'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}
