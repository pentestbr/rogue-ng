from requests import RequestProcessor

class Server:

	def __init__(self):
		self.enabled = False #todo: detect rather than insist
		self.requests = {}
		self.request_processor = RequestProcessor()

	def create_request(self, action):
		if self.request_processor.isValid(action):
			if len(self.requests) == 0:
				id = 1
			else:
				id = int(max(self.requests.keys()))+1
			req = {'id': id,
			       'action': action,
			       'complete': False}
			self.requests[id] = req
			return req
		else:
			raise InvalidActionException("Unknown action: "+action)

	def get_requests(self):
		return self.requests.values()
