#!/usr/bin/env python

"""Scrape the ActiveBlog"""

import re
import feedparser
from madcow.util import Module
import urllib
from urlparse import urljoin

class Main(Module):

    pattern = re.compile(u'^\s*(active)?blog\s*$', re.I)
    require_addressing = False
    help = u'activeblog|blog - get the latest blog post from ActiveState'
    error = u'Looks like the blog isn\'t co-operating today.'

    _rss_url = u'http://www.activestate.com/blog/rss.xml'

    def response(self, nick, args, kwargs):
        entries = feedparser.parse(self._rss_url).entries
        if entries:
            item = entries[0]
            return u'\n'.join([item.title, item.link, item.updated])
        else:
            return u'%s' % (self.error)
