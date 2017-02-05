from pyfiglet import Figlet

from core import ApiClient
from commands import Help, Quit

class Command:

	def init_commands(self):
		self.cmd_handlers = {
			'help': Help(),
			'quit': Quit(),
			'exit': Quit()
		}


	def __init__(self):
		self.core_url = 'http://localhost:5000/api'
		self.client = ApiClient(self.core_url)
		self.init_commands()

	def intro(self):
		f = Figlet()
		print 'Welcome to:'
		print f.renderText('rogue-ng')
		print 'Configured server: '+ self.core_url

		if self.client.check_status():
			status = 'Connected'
		else:
			status = 'Not connected'
		print 'Connection status: '+status

	def get_command(self):
		prompt = 'rogue-ng> '
		cmd = raw_input(prompt)
		return cmd

	def execute_command(self, cmd):
		handler = self.cmd_handlers[cmd]
		handler.execute()


	def run(self):
		self.intro()
		while True:
			cmd = self.get_command()
			self.execute_command(cmd)
