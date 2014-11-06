# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - api is an example of Hypermedia API support and access control
#########################################################################

def index():
    """
    Put your code and select translate language to use bing translator to
    translate
    """

    response.flash = T("Welcome to Web2py Translate!")

    form = SQLFORM.factory(Field('file', 'text', requires=IS_NOT_EMPTY()))
    if form.process().accepted:
        try:
            session.file = dict()
            lang_file = eval(form.vars.file)
            for key in lang_file:
                if key:
                    session.file[base64.standard_b64encode(key)] = lang_file[key]
        except:
            response.flash = T("Wrong file format... Try again")
        redirect(URL('translate'))
    return dict(form=form)

def translate():
    import textwrap
    fields = list()
    for key in session.file:
        fields.append(Field(key, 'text',
                            default=session.file[key],
                            label=XML('<br>'.join(textwrap.wrap(base64.standard_b64decode(key),100)))))

    form = SQLFORM.factory(*fields)

    if form.accepts(request.vars, session, keepvalues=True):
        for enc_translates in session.file:
            session.file[enc_translates] = form.vars[enc_translates]

    return dict(form=form)

def do_automatic():

    if request.vars._from and request.vars._to:
        for key in session.file:
            if base64.standard_b64decode(key) == session.file[key] or not session.file[key]:
                session.file[key] = _automatic_translate(session.file[key],
                                                         request.vars._from,
                                                         request.vars._to)[4:-1]  # removing trash

    redirect(URL('translate'))

def _automatic_translate(_text, _from, _to):
    import json
    import requests
    import urllib
    args = {
            'client_id': CLIENT_ID,#your client id here
            'client_secret': CLIENT_SECRET,#your azure secret here
            'scope': 'http://api.microsofttranslator.com',
            'grant_type': 'client_credentials'
    }
    oauth_url = 'https://datamarket.accesscontrol.windows.net/v2/OAuth2-13'
    oauth_junk = json.loads(requests.post(oauth_url, data=urllib.urlencode(args)).content)
    translation_args = {
            'text': _text,
            'to': _to,
            'from': _from
    }
    headers = {'Authorization': 'Bearer '+oauth_junk['access_token']}
    translation_url = 'http://api.microsofttranslator.com/V2/Ajax.svc/Translate?'
    translation_result = requests.get(translation_url+urllib.urlencode(translation_args), headers=headers)
    return translation_result.content

def export():
    translated_file = dict()
    for item in session.file:
        translated_file[base64.standard_b64decode(item)] = session.file[item]
    return dict(t_file=translated_file)
