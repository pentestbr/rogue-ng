from datetime import datetime

from exceptions import InvalidActionException, UnknownModule
from request_processing import RequestProcessor

import modules

class Server:

	def __init__(self):
		self.enabled = False #todo: detect rather than insist
		self.request_processor = RequestProcessor()
		self.modules={}
		self.load_modules()


	def load_modules(self):
		self.module_handlers = {
			'hotspot': modules.hotspot.Hotspot(),
			'mitmf': modules.mitmf.Mitmf(),
			'beef': modules.beef.Beef()
		}
		for name in self.module_handlers.keys():
			self.modules[name] = {'name':name, 'config':None, 'used':False}

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

	def update_module(self, name, config, used):
		if name not in self.modules.keys(): raise UnknownModule(name)
		module = {'name':name, 'config':config, 'used': used}
		self.modules[name] = module
		return module

	def get_modules(self):
		return self.modules.values()

