# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

import base64
import os

response.logo = A(B('web',SPAN(2), 'py_translate'),
                  _class="brand", _href="https://github.com/dmvieira/web2py-translate")
response.title = request.application.replace('_', ' ').title()
response.subtitle = ''


response.menu = [
    (T('Home'), False, URL('default', 'index'), [])
]

CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')

