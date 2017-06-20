import webapp2
import helpers
from google.appengine.ext import db

#### Database Models
from models.user import User
from models.blog import Blog
from models.comment import Comment

#### Handlers
from handlers.registration import Registration
from handlers.signup import Signup
from handlers.logout import Logout
from handlers.login import Login
from handlers.welcome import Welcome
from handlers.newblog import NewBlog
from handlers.blogpage import BlogPage
from handlers.allblogs import AllBlogs
from handlers.editblog import EditBlog
from handlers.deleteblog import DeleteBlog
from handlers.likeblog import LikeBlog
from handlers.deletecomment import DeleteComment
from handlers.editcomment import EditComment

#### Routing
app = webapp2.WSGIApplication([
    ('/blog', Welcome),
    ('/blog/registration', Registration),
    ('/blog/logout', Logout),
    ('/blog/login', Login),
    ('/blog/welcome', Welcome),
    ('/blog/newblog', NewBlog),
    ('/blog/([0-9]+)', BlogPage),
    ('/blog/allblogs', AllBlogs),
    ('/blog/editblog/([0-9]+)', EditBlog),
    ('/blog/deleteblog/([0-9]+)', DeleteBlog),
    ('/blog/like/([0-9]+)', LikeBlog),
    ('/blog/deletecomment/([0-9]+)/([0-9]+)', DeleteComment),
    ('/blog/editcomment/([0-9]+)/([0-9]+)', EditComment)],
    debug=True)
