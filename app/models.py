from google.appengine.ext import db

ROLE_USER = 0
ROLE_ADMIN = 1

class User(db.Model):
    id = db.StringProperty(required = True)
    nickname = db.StringProperty(required = True)
    email = db.StringProperty(required = True)
    role = db.StringProperty(required = True)
    about_me = db.StringProperty(required = True)
    last_seen = db.DateTimeProperty(auto_now_add = True)


class Post(db.Model):
    title = db.StringProperty(required = True)
    content = db.TextProperty(required = True)
    when = db.DateTimeProperty(auto_now_add = True)
    author = db.UserProperty(required = True, indexed=True)
    image = db.StringProperty()


"""    author = db.ReferenceProperty(User, collection_name='posts')
"""
