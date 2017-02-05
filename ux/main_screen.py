from curses import initscr
from pyfiglet import Figlet

from core import ApiClient

class MainScreen:

	def __init__(self):
		self.core_url = 'http://localhost:5000/api'
		self.client = ApiClient(self.core_url)


	def intro(self):
		f = Figlet()
		self.scr.addstr(0, 0, f.renderText('rogue-ng'))
		self.scr.addstr(0, 0, 'Welcome to:')
		self.scr.addstr(8, 5, 'Configured server: '+ self.core_url)

		self.scr.addstr(9, 5, 'Connection       : Trying..')
		self.scr.refresh()
		if self.client.check_status():
			status = 'Connected'
		else:
			status = 'No connection'

		self.scr.addstr(9, 24, status)
		self.scr.addstr(12, 5, 'Press any key to continue')

	def run(self, scr):
		self.scr = scr
		scr.clear()
		self.intro()
		scr.refresh()
		scr.getkey()
