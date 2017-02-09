from basic import BaseCommand as base
from core import ApiClient

class ServerOps(base):

	def send_start_request(self):
		print 'Requesting server to start..'
		client = ApiClient(self.console.core_url)
		client.request_start()

	def send_stop_request(self):
		print 'Requesting server to stop..'
		client = ApiClient(self.console.core_url)
		client.request_stop()

	def check_status(self, state):
		client = ApiClient(self.console.core_url)
		status = client.check_status()
		if status['status'] != 'Live':
			print 'No connection to server'
			return False
		elif status['enabled'] and not state:
			print 'Server is alreadyrunning'
			return False
		elif not status['enabled'] and state:
			print 'Server is not running'
			return False
		else:
			return True

class Start(ServerOps):
	def execute(self, params=None):
		if self.check_status(False):
			self.send_start_request()

class Stop(ServerOps):
	def execute(self, params=None):
		if self.check_status(True):
			selfsend_stop_request()

class ServerUrl(base):
	def execute(self, params=None):
		if not params:
			print 'missing parameter <url>'
		else:
			self.console.core_url = params[0]
			print 'Server URL set to:', self.console.core_url
