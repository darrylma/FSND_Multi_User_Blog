from handlers.handler import Handler

#### Handles welcome page
class Welcome(Handler):
	#Displays welcome page afer user logs in
	def get(self):
		if self.user:
			self.render('welcome-form.html', username = self.user.name)
		else:
			self.redirect('/blog/login')
