from handlers.handler import Handler
from models.user import User
from helpers import *

#### Handles user creation process
class Signup(Handler):
	#Displays sign up page for user to key in details
	def get(self):
		self.render("signup-form.html")

	#Creates new user based on input
	def post(self):
		have_error = False
		self.username = self.request.get('username')
		self.password = self.request.get('password')
		self.verify = self.request.get('verify')
		self.email = self.request.get('email')

		#Checks that all input has valid format, else throws an error
		params = dict(username = self.username, email = self.email)

		if not valid_username(self.username):
			params['error_username'] = "That's not a valid username."
			have_error = True

		if not valid_password(self.password):
			params['error_password'] = "That's not a valid password."
			have_error = True

		elif self.password != self.verify:
			params['error_verify'] = "Your passwords didn't match."
			have_error = True

		if not valid_email(self.email):
			params['error_email'] = "That's not a valid email."
			have_error = True

		#Checks that all info provided is valid before proceeding to create user
		if have_error:
			self.render('signup-form.html', **params)
		else:
			self.done()

	def done(self, *a, **kw):
		raise NotImplementedError
