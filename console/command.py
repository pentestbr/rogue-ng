from pyfiglet import Figlet

from core import ApiClient
from commands import Help, Status, Quit
from commands import Start, Stop, ServerUrl
from commands import Config, Use, Remove

class Command:

	def init_commands(self):
		self.cmd_handlers = {
			'help': Help(),
			'server': ServerUrl(),
			'start': Start(),
			'stop': Stop(),
			'status': Status(),
			'quit': Quit(),
			'exit': Quit(),
			'config': Config(),
			'use': Use(),
			'remove': Remove()
		}

		for cmd in self.cmd_handlers:
			self.cmd_handlers[cmd].console = self

	def __init__(self):
		self.core_url = 'http://localhost:5000/api'
		self.client = ApiClient(self.core_url)
		self.init_commands()

	def intro(self):
		f = Figlet()
		print ''
		print 'Welcome to:'
		print f.renderText('rogue-ng')
		print ''
		self.cmd_handlers['status'].execute()
		print ''
		print 'Use \'help\' to see commands'

	def get_command(self):
		prompt = 'rogue-ng> '
		cmd = raw_input(prompt)
		return cmd

	def execute_command(self, line):
		words = line.split()
		cmd = words[0]
		params = words[1:]
		try:
			handler = self.cmd_handlers[cmd]
		except KeyError:
			if cmd != '':
				print 'Unknown cmd \'',cmd,'\''
		else:
			#print ''
			handler.process(cmd, params)
			#print ''

	def run(self):
		self.intro()
		while True:
			cmd = self.get_command()
			self.execute_command(cmd)
