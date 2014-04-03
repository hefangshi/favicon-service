# -*- coding: utf-8 -*-

import tornado.wsgi
import urlparse
import urllib2
import sae.storage
import pylibmc as memcache
import time

STORAGE_DOMAIN = 'icon'
DEFAULT_ICON = 'http://favicon-icon.stor.sinaapp.com/default.ico'
STORAGE_PATH = 'http://favicon-icon.stor.sinaapp.com/'


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("favicon service")


class IconHandler(tornado.web.RequestHandler):
    def get(self, **params):
        mem = memcache.Client()
        url = self.getHost(params['url'])
        key = '%s.ico' % hash(url)
        cache_date = mem.get(key)
        if cache_date == 'INVALID' or url is False:
            self.redirect(DEFAULT_ICON)
            return
        elif cache_date is not None:
            self.redirect("%s%s" % (STORAGE_PATH, key))
            return
        try:
            response = urllib2.urlopen('%s/favicon.ico' % url, timeout=3)
            if 'image' not in response.info().maintype:
                raise 'invalid type'
            icon = response.read()
            ob = sae.storage.Object(icon)
            client = sae.storage.Client()
            client.put('icon', key, ob)
            mem.set(key, time.time())
        except:
            mem.set(key, 'INVALID')
            self.redirect(DEFAULT_ICON)
            return
        self.redirect("%s%s" % (STORAGE_PATH, key))

    def getHost(self, url):
        parsed = urlparse.urlparse(url)
        if parsed.netloc is None:
            return False
        scheme = parsed.scheme
        if parsed.scheme is None:
            scheme = 'http'
        if parsed.netloc == 'feedburner.google.com':
            return False
        return "%s://%s" % (scheme, parsed.netloc)
