from google.appengine.ext import db
from helpers import *

#### Defines blog database model
class Blog(db.Model):
	title = db.StringProperty(required = True)
	contents = db.TextProperty(required = True)
	created = db.DateTimeProperty(auto_now_add = True)
	created_by = db.StringProperty(required = False)
	last_modified = db.DateTimeProperty(auto_now = True)
	likes = db.StringListProperty()

	def render(self):
		self._render_text = self.contents.replace('\n', '<br>')
		return render_str("blogpage-form.html", blog = self)

	#Checks that blog exists in database and returns blog entity if it does
	@classmethod
	def check_if_valid_post(cls, post_id):
		key = db.Key.from_path('Blog', int(post_id), parent=blog_key())
		blog = db.get(key)
		if blog :
			return blog

	#checks if user created the blog and returns blog if he/she did 
	@classmethod
	def check_if_user_owns_post(cls, post_id, username):
		blog = cls.check_if_valid_post(post_id)
		if blog and blog.created_by == username:
			return blog
