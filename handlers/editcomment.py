from google.appengine.ext import db
from handlers.handler import Handler
from models.blog import Blog
from models.comment import Comment
from helpers import *


#### Handles editing of a comment
class EditComment(Handler):
	#Displays form to edit comment if comment is owned by user
	def get(self, post_id, comment_id):
		#Checks if user is logged in
		if self.user:
			valid_comment = Comment.check_if_valid_comment(comment_id)
			#Checks if comment exists
			if valid_comment:
				key = db.Key.from_path('Comment', int(comment_id), parent=blog_key())
				comment = db.get(key)
				#Check if comment is created by user before navigating to edit comment form
				if comment.created_by == self.user.name:
					self.render("editcomment-form.html", comment = comment, post_id = post_id)
				else:
					error = "You cannot edit a comment that was created by someone else!"
					self.render("blogpage-form.html", error_header = error)
			else:
				error = "You cannot edit a comment that does not exist"
				self.render("welcome-form.html", error_header = error)
		else:
			self.redirect('/blog/login')

	#Updates comment content in database
	def post(self, post_id, comment_id):
		blog = Blog.check_if_valid_post(post_id)
		valid_comment = Comment.check_if_valid_comment(comment_id)
		#Checks if user is logged in
		if self.user:
			#Checks if comment exists
			if valid_comment:
				comment = Comment.check_if_user_owns_comment(comment_id, self.user.name)
				#Checks if blog is valid and comment is owned by user before allowing to edit comment
				if blog and comment:
					comment_content = self.request.get('comment')
					#Checks if comment conent is not empty before commiting changes to database
					if comment_content:
						comment.comment = comment_content
						comment.put()
						self.redirect('/blog/%s' % post_id)
					else:
						error = "Please input comment"
						self.render("editcomment-form.html", error = error, comment = comment)
				else:
					error = "You cannot edit a comment that was created by someone else!"
					self.render("editcomment-form.html", error_header = error)
			else:
				error = "You cannot edit a comment that does not exist"
				self.render("welcome-form.html", error_header = error)
		else:
			self.redirect('/blog/login')
