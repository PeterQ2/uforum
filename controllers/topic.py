def new():
    forum_id = request.args(0)
    db.topic.forum_name.default = forum_id
    db.topic.forum_name.readable = False
    db.topic.forum_name.writable = False
    db.topic.slotje.readable = False
    db.topic.slotje.writable = False
    db.topic.views.readable = False
    db.topic.views.writable = False
    db.topic.last_updated.readable = False
    db.topic.last_updated.writable = False
    form = SQLFORM(db.topic)
    if form.process().accepted:
        db(db.auth_user.id == auth.user.id).update(forum_posts=db.auth_user.forum_posts+1)
        redirect(URL('topic','read',args=form.vars.id))
    return dict(form=form, error=response.flash)

def read():
    topic_id = request.args(0)

    if not topic_id:
        redirect(URL('default','index'))

    form = FORM(TEXTAREA(_name='reply_text', requires=IS_NOT_EMPTY()),
                BR(),
                INPUT(_type='submit',_value='Plaats reactie'))

    if form.process().accepted:
        form.vars['topic_title'] = topic_id
        db.topic_reply.insert(**form.vars)
        db(db.topic.id == topic_id).update(last_updated = request.now)

    topic = db(db.topic.id == topic_id).select().first()
    user = db(db.auth_user.id == topic.created_by).select().first()
    forum = db(db.forum.id == topic.forum_name).select().first()
    db(db.topic.id == topic_id).update(views=db.topic.views+1)

    p = pagination()
    p.items_per_page = settings.topic_reply_per_page
    p.records = db(db.topic_reply.topic_title == topic_id).count()
    reply = db(db.topic_reply.topic_title == topic_id).select(orderby=~db.topic_reply.created_on, limitby=p.limitby())

    return dict(topic=topic,user=user,forum=forum,reply=reply,count_replys=p.records,pagination=p,form=form)

def active():
    p = pagination()
    p.items_per_page = settings.category_topic_per_page
    p.records = db(db.topic).count()
    topic = db(db.topic).select(orderby=~db.topic.last_updated,limitby=p.limitby())
    return dict(topic=topic, count=p.records, pagination=p)

@auth.requires_membership('admin')
def close_topic():
    topic_id = request.args(0)
    db(db.topic.id == topic_id).update(slotje='On')
    redirect(URL('topic','read',args=topic_id))

@auth.requires_membership('admin')
def open_topic():
    topic_id = request.args(0)
    db(db.topic.id == topic_id).update(slotje='Off')
    redirect(URL('topic','read',args=topic_id))

@auth.requires_membership('admin')
def edit_topic():
    topic_id = request.args(0)
    topic = db(db.topic.id == topic_id).select().first()
    forum = db(db.forum.id == topic.forum_name).select().first()
    form = SQLFORM(db.topic, topic_id)
    if form.process().accepted:
        redirect(URL('topic','read',args=topic_id))
    return dict(forum=forum, topic=topic, form=form)

@auth.requires_membership('admin')
def remove_topic():
    topic_id = request.args(0)
    topic = db(db.topic.id == topic_id).select().first()
    db(db.topic.id == topic_id).delete()
    redirect(URL('default','category',args=topic.forum_name))

@auth.requires_membership('admin')
def remove_reply():
    reply_id = request.args(0)
    reply = db(db.topic_reply.id == reply_id).select().first()
    db(db.topic_reply.id == reply_id).delete()
    redirect(URL('topic','read',args=reply.topic_title))