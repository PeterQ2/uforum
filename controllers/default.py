# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################


def index():
    category = db(db.category).select()
    ct = db(db.topic).count()
    cr = db(db.topic_reply).count()
    cl = db(db.auth_user).count()
    user = db(db.auth_user.id == cl).select().first()
    stats = T('Amount topics') + ": <span>%s</span> " % (ct) + T('Amount topic replys') + ": <span>%s</span> "  % (cr) + T('Amount members') + ": <span>%s</span> " % (cl)
    if cl > 0:
        stats += T('Newest member') + ": <a href='" + URL('user', 'profile', args=cl) + "'>%s</a>" % (user.username)

    return dict(category=category, stats=stats, user=user)

def category():
    forum_id = request.args(0)
    forum = db(db.forum.id == forum_id).select().first()

    p = pagination()
    p.items_per_page = settings.category_topic_per_page
    p.records = db(db.topic.forum_name == forum_id).count()
    topic = db(db.topic.forum_name == forum_id).select(limitby=p.limitby())

    return dict(title=forum.name, topic=topic, count=p.records, pagination=p)

def user():
    return dict(form=auth())

@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())
