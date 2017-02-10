from pyfiglet import Figlet
import readline

from core import ApiClient
from completer import RogueCompleter
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

	def init_completion(self):
		readline.parse_and_bind('tab: complete')
		completer = RogueCompleter(self.cmd_handlers.keys())
		readline.set_completer(RogueCompleter(self.cmd_handlers).complete)

	def __init__(self):
		self.core_url = 'http://localhost:5000/api'
		self.client = ApiClient(self.core_url)
		self.init_commands()
		self.init_completion()

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
			if cmd: self.execute_command(cmd)
