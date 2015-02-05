import mechanize
from bs4 import BeautifulSoup

_CHORE_URL = 'https://www.choremonster.com/kids/chores'
_LOGIN_URL = 'https://www.choremonster.com/kids/login'

class ChoreMonster:
	def kids_login(self, user, password):
		self.browser = mechanize.Browser()
		self.browser.open(_LOGIN_URL)
		self.browser.select_form(predicate = lambda form: form.attrs.get('id') == "new_child")
		self.browser["child[username]"] = user
		self.browser["child[password]"] = password
		response = self.browser.submit()
		# Should get redirected to chores
		if response.geturl() != _CHORE_URL:
			raise Exception("Couldn't login (URL: " + response.geturl() + ")")

	def get_chores(self):
		response = self.browser.open(_CHORE_URL)
		if response.geturl() != _CHORE_URL:
			raise Exception("Couldn't fetch chores (URL: " + response.geturl() + ")")

		soup = BeautifulSoup(response.get_data())

		chores = {}
		for chore in soup.find_all('a', class_='chore_show'):
			chore_classes = [c for c in chore['class'] if c != 'chore_show']
			if len(chore_classes) != 1:
				raise Exception("Unknown chore class: " + str(chore_classes))

			chore_name = chore.findChild("div", class_="name").getText()
			chores.setdefault(chore_classes[0], []).append(chore_name)

		return chores
