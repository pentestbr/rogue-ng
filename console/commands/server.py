from basic import BaseCommand as base

class Start(base):
	def execute(self, params=None):
		print 'Server started'

class Stop(base):
	def execute(self, params=None):
		print 'Server stopped'

class ServerUrl(base):
	def execute(self, params=None):
		if not params:
			print 'missing parameter <url>'
		else:
			self.console.core_url = params[0]
			print 'Server URL set to:', self.console.core_url
