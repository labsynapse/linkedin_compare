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
    from base64 import standard_b64encode
    form = SQLFORM.factory(Field('links', 'list:string',
                                 label='Write here LinkedIn Public urls',
                                 requires=IS_URL()))
    link = None
    if form.process().accepted:
        links = form.vars.links
        if not isinstance(links, list):
            links = [links]
        link = URL('default', 'view', args=standard_b64encode(','.join(links)),
                   scheme=True)
    return dict(form=form, link=link)

def view():
    from base64 import standard_b64decode
    import BeautifulSoup
    from gluon.storage import Storage
    import urllib2
    import HTMLParser

    if request.args(0):
        try:
            links = standard_b64decode(request.args(0)).split(',')
        except:
            raise HTTP(400)

        compare_guys = Storage()
        html = HTMLParser.HTMLParser()
        for link in links:
            if link:
                if not link.startswith('http'):
                    link = 'http://'+link
                compare_guys[link] = Storage()
                opener = urllib2.build_opener()
                opener.addheaders = [('User-agent', 'Mozilla/5.0')]
                response = opener.open(link)
                html_content = response.read()
                soup = BeautifulSoup.BeautifulSoup(html_content)

                image_div = soup.findChild("div", {"class": "profile-picture"})
                if image_div:
                    img_link = dict(image_div.find('img').attrs)
                    if img_link:
                        compare_guys[link].image = img_link['src']

                name = soup.find("span", {"class": "full-name"})
                if name:
                    compare_guys[link].name = html.unescape(name.text)
                description = soup.find("p", {"class": "description"})
                if description:
                    compare_guys[link].description = html.unescape(description.text)

                skills = soup.findAll("span", {"class": "endorse-item-name-text"})
                compare_guys[link].skills = list()
                for skill in skills:
                    if skill.text:
                        compare_guys[link].skills.append(html.unescape(skill.text))
    else:
        raise HTTP(400)

    return dict(compare_guys=compare_guys)