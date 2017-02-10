from basic import BaseCommand as base
from core import ApiClient

class Config(base):

	def execute(self, params=None):
		print "config: ", params

class Use(base):
	def execute(self, params=None):
		client = ApiClient(self.console.core_url)
		for name in params:
			client.load_module(name)

class Remove(base):
	pass
