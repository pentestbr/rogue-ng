from basic import BaseCommand as base
from core import ApiClient

class Config(base):

	def __init__(self):
		self.modules = []

	def reload(self):
		client = ApiClient(self.console.core_url)
		self.modules = client.list_modules()
		print 'Just reloaded module list: {}'.format(self.modules)

	def execute(self, params=None):
		print "config: ", params

	def match_modules(self, text):
		return [x for x in self.modules if x.startswith(text)]

	def check_status(self):
		client = ApiClient(self.console.core_url)
		status = client.check_status()
		if status['status'] == 'Live':
			return True
		else:
			print 'No connection to server. Check url.'
			return False

	def complete(self, line, text):
		return self.match_modules(text)

class Use(Config):
	def execute(self, params=None):
		if self.check_status():
			client = ApiClient(self.console.core_url)
			for name in params:
				return client.load_module(name)
#				if msg: print msg


class Remove(Config):
	def execute(self, params=None):
		if self.check_status():
			client = ApiClient(self.console.core_url)
			for name in params:
				client.remove_module(name)

