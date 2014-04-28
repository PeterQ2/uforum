def profile():
    user_id = request.args(0)
    user = db(db.auth_user.id==user_id).select().first()
    topic = db(db.topic.created_by==user_id).select()
    count = db(db.topic.created_by==user_id).count()
    return dict(user=user,topic=topic,count=count)

def memberlist():
    users = db(db.auth_user).select()
    return dict(user=users)