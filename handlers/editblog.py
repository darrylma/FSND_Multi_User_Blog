from handlers.handler import Handler
from models.blog import Blog
from helpers import *
import time

#### Handles editing of a blog
class EditBlog(Handler):
    #Displays form to edit blog if blog is owned by user
    def get(self, post_id):
        #Checks user is logged in
        if self.user:
            blog = Blog.check_if_user_owns_post(post_id, self.user.name)
            #Checks if blog belongs to user before navigating to edit blog form
            if blog:
                self.render("editblog-form.html", blog=blog)
            else:
                error = "You cannot edit a blog that was created by someone else!"
                self.render("allblogs-form.html", error_header = error)
        else:
            self.redirect('/blog/login')

    #Updates blog title and content in database
    def post(self, post_id):
        #Checks user is logged in
        if self.user:
            blog = Blog.check_if_user_owns_post(post_id, self.user.name)
            #Checks if blog belongs to user before allowing user to edit blog
            if blog:
                title = self.request.get("title")
                contents = self.request.get("contents")
                #Checks if title and contents are not empty before committing changes to database
                if title and contents:
                    blog.title = title
                    blog.contents = contents
                    blog.put()
                    time.sleep(0.5)
                    self.redirect('/blog/allblogs')
                else:
                    error = "Please provide both a title and contents!"
                    self.render("editblog-form.html", blog = blog, error = error)
            else :
                error = "You cannot edit a blog that was created by someone else!"
                self.render("allblogs-form.html", error_header = error)
        else:
			self.redirect('/blog/login')
