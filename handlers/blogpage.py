from google.appengine.ext import db
from handlers.handler import Handler
from models.blog import Blog
from models.comment import Comment
from helpers import *
import time

#### Displays one blog and all associated comments and allows user to post comment
class BlogPage(Handler):
	def get(self, post_id):
		blog = Blog.check_if_valid_post(post_id)
		#Displays blog if it exists
		if blog:
			comments = db.GqlQuery("select * from Comment where post_id = " + post_id + " order by created desc")
			comments_num = comments.count()
			self.render("blogpage-form.html", blog = blog, comments = comments, comments_num = comments_num)
		else:
			self.error(404)
			return

	def post(self, post_id):
		blog = Blog.check_if_valid_post(post_id)
		if blog:
			#Allows user to post comment if logged in, else redirects user to login page
			if self.user:
				key = db.Key.from_path('Blog', int(post_id), parent=blog_key())
				blog = db.get(key)
				comment_content = self.request.get('comment')
				created_by = self.user.name

				#Checks that comment box is not empty
				if comment_content:
					#Creates new comment entity
					comment = Comment(parent = blog_key(), comment = comment_content, post_id = int(post_id), created_by = created_by)
					comment.put()

					#Queries for all comments associated with blog and displays below
					comments = db.GqlQuery("select * from Comment where post_id = " + post_id + "order by created desc")
					time.sleep(0.5)
					self.render("blogpage-form.html", blog = blog, comments = comments)
				else:
					comments = db.GqlQuery("select * from Comment where post_id = " + post_id + "order by created desc")
					error = "Please input comment"
					self.render("blogpage-form.html", blog = blog, comments = comments, error = error)
			else:
				self.redirect('/blog/login')
		else:
			self.error(404)
			return
