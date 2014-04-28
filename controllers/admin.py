def index():
    grid = SQLFORM.smartgrid(db.category)
    return dict(grid=grid)

def forum():
    response.view = 'admin/index.html'
    grid = SQLFORM.smartgrid(db.forum)
    return dict(grid=grid)

def topic():
    response.view = 'admin/index.html'
    grid = SQLFORM.smartgrid(db.topic)
    return dict(grid=grid)

def topic_reply():
    response.view = 'admin/index.html'
    grid = SQLFORM.smartgrid(db.topic_reply)
    return dict(grid=grid)