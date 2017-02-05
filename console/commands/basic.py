import sys
from core import ApiClient

class Help:
	def execute(self):
		print 'recon-ng 2017'
		print 'Useful commands:'
		print '\thelp        Pretty frickin obvious. You typed it to get here'
		print '\tquit        Exits the console (also \'exit\')'
		print '\tstatus      Shows status of connection to server'
class Quit:
	def execute(self):
		sys.exit()


class Status:
	def execute(self):
		client = ApiClient(self.console.core_url)
		if client.check_status():
			status = "Connected"
		else:
			status = "Not connected"
		print 'Configured server: ', self.console.core_url
		print 'Connection status: ', status
