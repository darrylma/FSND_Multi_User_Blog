from google.appengine.ext import db
from handlers.handler import Handler
from models.blog import Blog
from helpers import *
import time

#### Deletes a blog
class DeleteBlog(Handler):
    def get(self, post_id):
        #Checks if user is logged in
        if self.user:
            blog = Blog.check_if_user_owns_post(post_id, self.user.name)
            #Checks if blog exists before proceeding to delete blog
            if blog:
                blog.delete()
                time.sleep(0.5)
                self.redirect('/blog/allblogs')
            else:
                error = "You cannot delete a blog that was created by someone else!"
                blogs = db.GqlQuery("select * from Blog order by created desc")
                self.render('allblogs-form.html', blogs = blogs, user = self.user, error_header = error)
        else:
            self.redirect('/blog/login')
