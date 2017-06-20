from handlers.handler import Handler
from models.user import User
from helpers import *

#### Handles login process
class Login(Handler):
	#Displays login form
	def get(self):
		self.render('login-form.html')
	#Logs user in
	def post(self):
		username = self.request.get('username')
		password = self.request.get('password')

		user = User.login(username, password)
		#Checks if user exists in database and password matches before navigating to welcome page
		if user:
			self.login(user)
			self.redirect('/blog/welcome')
		else:
			msg = "Invalid login"
			self.render('login-form.html', username = username, error = msg)
