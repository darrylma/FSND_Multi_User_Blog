from handlers.handler import Handler
from handlers.signup import Signup
from models.user import User
from helpers import *

#### Handles registration process
class Registration(Signup):
    def done(self):
        #Checks that user does not already exist before proceeding to sign user up
        u = User.by_name(self.username)
        if u:
            msg = 'That user already exists.'
            self.render('signup-form.html', error_username = msg)
        else:
            u = User.register(self.username, self.password, self.email)
            u.put()

            self.login(u)
            self.redirect('/blog/welcome')
