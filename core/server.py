from datetime import datetime

from exceptions import InvalidActionException
from request_processing import RequestProcessor

class Server:

	def __init__(self):
		self.enabled = False #todo: detect rather than insist
		self.request_processor = RequestProcessor()
		self.modules={}

	def create_request(self, action):
		if self.request_processor.isValid(action):
			if len(self.request_processor.requests) == 0:
				id = 1
			else:
				id = int(max(self.request_processor.requests.keys()))+1
			req = {'id': id,
				'created': datetime.now(),
			       'action': action,
			       'complete': False}
			self.request_processor.requests[id] = req
			return req
		else:
			raise InvalidActionException("Unknown action: "+action)

	def get_requests(self):
		return self.request_processor.requests.values()

	def add_module(self, name, config):
		module = {'name':name, 'config':config}
		self.modules[name] = module
		return module

	def get_modules(self):
		return self.modules.values()
