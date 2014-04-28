from plugin_ckeditor import CKEditor
ckeditor = CKEditor(db)
ckeditor.define_tables()

db.define_table(
    'category',
    Field('name')
)
db.define_table(
    'forum',
    Field('category_name', requires=IS_IN_DB(db,db.category.id,'%(name)s')),
    Field('name', 'string', requires=IS_NOT_EMPTY()),
    Field('description', 'text', requires=IS_NOT_EMPTY())
)
db.define_table(
    'topic',
    Field('forum_name', requires=IS_IN_DB(db,db.forum.id,'%(name)s')),
    Field('title', 'string', requires=IS_NOT_EMPTY()),
    Field('topic_text', 'text', requires=IS_NOT_EMPTY(), widget=ckeditor.widget),
    Field('views', 'integer', default='0'),
    Field('slotje', default='Off', requires=IS_IN_SET(['On', 'Off'])),
    Field('last_updated', 'datetime',default=request.now),
    auth.signature
)
db.define_table(
    'topic_reply',
    Field('topic_title', requires=IS_IN_DB(db,db.topic.id,'%(title)s')),
    Field('reply_text', 'text', requires=IS_NOT_EMPTY()),
    auth.signature
)
