# -*- coding: utf-8 -*-

import handler

route = [
    (r"/", handler.MainHandler),
    (r"/domain/(?P<url>.*)", handler.IconHandler),
]
