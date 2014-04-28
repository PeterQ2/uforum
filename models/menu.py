# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

import time

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.logo = B('Forum')
response.title = request.application.replace('_',' ').title()

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Your Name <you@example.com>'
response.meta.keywords = 'web2py, python, framework'
response.meta.generator = 'Web2py Web Framework'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [
    (T('Home'), False, URL('default', 'index'), []),
    (T('Active topics'), False, URL('topic', 'active',), []),
    (T('Memberlist'), False, URL('user', 'memberlist'), [])
]
if auth.has_membership('admin'):
    response.menu += [(T('Admin'), False, URL('admin','index'), [])]


#########################################################################
###  @todo   Online controle tijd (timestamp)
#########################################################################

## if auth.is_logged_in():
##    db(db.auth_user.id == auth.user.id).update(id=1)