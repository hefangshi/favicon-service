# -*- coding: utf-8 -*-
import os
import tornado.wsgi
import sae
import urls

settings = {
    #"static_path": os.path.join(os.path.dirname(__file__), "static"),
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
    "gzip": True,
    "debug": True,
}
#只有 template_path 是必要，其它可以忽略
app = tornado.wsgi.WSGIApplication(urls.route, **settings)
application = sae.create_wsgi_app(app)
