from google.appengine.ext import db
from helpers import *

#Defines user database model
class User(db.Model):
    name = db.StringProperty(required = True)
    pw_hash = db.StringProperty(required = True)
    email = db.StringProperty()

    #Returns user based on user_id provided
    @classmethod
    def by_id(cls, uid):
        return User.get_by_id(uid, parent = users_key())

    #Returns user based on username provided
    @classmethod
    def by_name(cls, name):
        u = User.all().filter('name =', name).get()
        return u

    #Masks password and returns user
    @classmethod
    def register(cls, name, pw, email = None):
        pw_hash = make_pw_hash(name, pw)
        return User(parent = users_key(),
                    name = name,
                    pw_hash = pw_hash,
                    email = email)

    #Checks that username and password matches and returns user entity if it does
    @classmethod
    def login(cls, name, pw):
        u = cls.by_name(name)
        if u and valid_pw(name, pw, u.pw_hash):
            return u
