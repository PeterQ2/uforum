from gluon.storage import Storage
settings = Storage()

settings.logo = B('Corebyte.Discus')
settings.title = request.application.replace('_',' ').title()

## read more at http://dev.w3.org/html5/markup/meta.name.html
settings.meta_author = 'Stefan van den Eertwegh <stefan.eertwegh@gmail.com>'
settings.meta_keywords = 'web2py, python, framework'
settings.meta_generator = 'Web2py Web Framework'

## your http://google.com/analytics id
settings.google_analytics_id = None

settings.topic_reply_per_page       = 5     # Aantal reacties per pagina : topic
settings.category_topic_per_page    = 20    # Aantal topics per pagina : categorie en actieve topics