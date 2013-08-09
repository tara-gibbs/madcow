"""Generate doc search links for Stackato Docs"""

import re
from madcow.util import Module
from madcow.util.text import *
import urllib
import os

try:
    import dbm
except ImportError:
    import anydbm as dbm
    
class Main(Module):
    pattern = re.compile(u'^\s*(docs)(?:\s+(.*)$)?')
    require_addressing = False
    help = u'docs                                       Link to the Stackato docs homepage\n\
             docs <searchterm>                          Generate a docs search link for the Stackato Docs'

    def response(self, nick, args, kwargs):
        cmd = args[0]
        search_term = args[1].strip() if args[1] else None
            
        if search_term:
            return u'%s: http://docs.stackato.com/search.html?%s' % ( nick, urllib.urlencode( {'q': search_term }) )
        else:
            return u'%s: http://docs.stackato.com/' % (nick)