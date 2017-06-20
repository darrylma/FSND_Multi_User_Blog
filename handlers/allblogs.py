from google.appengine.ext import db
from handlers.handler import Handler

#### Displays all blogs
class AllBlogs(Handler):
    def get(self):
        #Return to login page if user not logged in
        if not self.user:
			self.redirect('/blog/login')
        else:
            blogs = db.GqlQuery("select * from Blog order by created desc")
            self.render("allblogs-form.html", blogs = blogs, user = self.user)
