from basic import BaseCommand as base

class Start(base):
	def execute(self):
		print 'Server started'

class Stop(base):
	def execute(self):
		print 'Server stopped'

class ServerUrl(base):
	def __init__(self):
		self.no_of_params = 1

	def execute(self, params):
		self.console.core_url = params[0]
		print 'Server URL set to:', self.console.core_url
