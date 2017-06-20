from handlers.handler import Handler

#### Handles log out
class Logout(Handler):
	#Displays logout form after user logs out
	def get(self):
		self.logout()
		self.render('logout-form.html')
