from basic import BaseCommand as base

class Config(base):

	def execute(self, params=None):
		print "config: ", params
