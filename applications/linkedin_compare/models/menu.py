# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

response.logo = A('Likedin Compare',
                  _class="brand", _href=URL('default', 'index'))
response.title = request.application.replace('_', ' ').title()
response.subtitle = ''


T.force('en')
