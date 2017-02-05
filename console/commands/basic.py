import sys
from core import ApiClient

class BaseCommand:

	def __init__(self):
		self.no_of_params = 0

	def process(self, cmd, params):
		if len(params) != self.no_of_params:
			print 'Invalid number of parameters, expecting', self.no_of_params
		else:
			self.cmd = cmd
			if not params:
				self.execute()
			else:
				self.execute(params)


class Help(BaseCommand):
	def execute(self):
		print 'recon-ng 2017'
		print 'Useful commands:'
		print '\thelp        Pretty frickin obvious. You typed it to get here'
		print '\tquit        Exits the console (also \'exit\')'
		print '\tstatus      Shows status of connection to server'
class Quit(BaseCommand):
	def execute(self):
		sys.exit()


class Status(BaseCommand):
	def execute(self):
		client = ApiClient(self.console.core_url)
		if client.check_status():
			status = "Connected"
		else:
			status = "Not connected"
		print 'Configured server: ', self.console.core_url
		print 'Connection status: ', status

class Test(BaseCommand):
	def __init__(self):
		self.no_of_params = 2

	def execute(self, params):
		print 'params sent are: ',params
