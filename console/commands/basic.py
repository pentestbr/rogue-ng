import sys
from core import ApiClient

class BaseCommand:

	def process(self, cmd, params):
		self.cmd = cmd
		if not params:
			self.execute()
		else:
			self.execute(params)

	def complete(self, line, text): return []

class Help(BaseCommand):
	def execute(self, params=None):
		print 'recon-ng 2017'
		print 'Useful commands:'
		print '\thelp           Pretty frickin obvious. You typed it to get here'
		print '\tquit           Exits the console (also \'exit\')'
		print ''
		print 'Server commmands:'
		print '\tserver <url>   Sets the server url to connect to'
		print '\tstatus         Shows the status of the server'
		print '\tstart          Starts the server\'s hotspot'
		print '\tstop           Stops the server\'s hotspot'
		print ''
		print 'Module commands:'
		print '\tuse <name>     Loads the named module'
		print '\tremove <name>  Removes the named module'
		print ''
		print 'Config commands:'
		print '\tconfig [all|module|field]   Configures the relevent area'
		print '\tinfo   [all|module|field]   Shows config for relevent area'

class Quit(BaseCommand):
	def execute(self, params=None):
		sys.exit()


class Status(BaseCommand):
	def execute(self, params=None):
		client = ApiClient(self.console.core_url)
		status = client.check_status()
		print 'Configured server: ', self.console.core_url
		print 'Connection status: ', status['status']
		print 'Server running   : ', status['enabled']
		print 'Modules enabled  :'
		for mod in status['modules']:
			print '\t {}'.format(mod)

class Test(BaseCommand):
	def execute(self, params=None):
		print 'params sent are: ',params
