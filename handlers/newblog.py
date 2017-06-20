from handlers.handler import Handler
from models.blog import Blog
from helpers import *
import time

#### Handles creation of a new blog
class NewBlog(Handler):
	#Displays new blog form for user to key in blog details
	def get(self):
		#Checks if user is logged in before navigating to new blog entry page
		if not self.user:
			self.redirect('/blog/login')
		self.render("newblog-form.html")

	#Captures blog information and creates new blog in database
	def post(self):
		#Checks if user exists before proceeding to create blog
		if self.user:
			title = self.request.get("title")
			contents = self.request.get("contents")
			created_by = self.user.name

			#Checks if title and content are not empty before proceeding to create blog
			if title and contents:
				blog = Blog(parent = blog_key(), title = title, contents = contents, created_by = created_by)
				blog.put()
				time.sleep(0.5)
				self.redirect('/blog/allblogs')
			else:
				error = "Please provide both a title and contents!"
				self.render("newblog-form.html", title = title, contents = contents, error = error)
		else:
			self.redirect('/blog/login')
