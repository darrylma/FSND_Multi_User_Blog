from google.appengine.ext import db
from handlers.handler import Handler
from models.comment import Comment
from helpers import *
import time

#### Deletes a comment
class DeleteComment(Handler):
    def get(self, post_id, comment_id):
        #Checks if user is logged in before allowing to delete comment
        if self.user:
            comment = Comment.check_if_user_owns_comment(comment_id, self.user.name)
            #Checks if comment is owned by user before allowing to delete comment
            if comment:
                comment.delete()
                time.sleep(0.5)
                self.redirect('/blog/%s' % post_id)
            else:
                error = "You cannot delete another person's comment"
                self.render("blogpage-form.html", error_header = error)
        else:
            self.redirect('/blog/login')
