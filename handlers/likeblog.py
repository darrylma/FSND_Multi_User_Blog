from handlers.handler import Handler
from models.blog import Blog
from helpers import *
import time

#### Handles like/dislike count of a each blog
class LikeBlog(Handler):
    def get(self, post_id):
        #Checks user is logged in
        if(self.user):
            blog = Blog.check_if_valid_post(post_id)
            uid = self.read_secure_cookie('user_id')
            #Checks if blog is valid
            if blog:
                #Checks if blof is owned by user and only allows user to like if blog is created by someone else
                if blog.created_by == self.user.name:
                    error = "You are not allowed to like your own post"
                    blogs = db.GqlQuery("select * from Blog order by created desc")
                    self.render('allblogs-form.html', blogs = blogs, user = self.user, error_header = error)
                #Removes user_id from blog's like list because user had already liked blog
                elif blog.likes and uid in blog.likes:
                    blog.likes.remove(uid)
                    blog.put()
                    time.sleep(0.5)
                    self.redirect(self.request.referer)
                #Adds user_id to blog's like list to keep track of number of likes
                else:
                    blog.likes.append(uid)
                    blog.put()
                    time.sleep(0.5)
                    self.redirect(self.request.referer)
            else:
                error = "You cannot like a blog that does not exist"
                self.render("welcome-form.html", error_header = error)
        else:
            self.redirect('/blog/login')
