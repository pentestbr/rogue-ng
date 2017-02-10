class RequestProcessor:

	def __init__(self):
		self.requests = {}

	def start(self):
		pass

	def stop(self):
		pass

	actions = { 'start': start,
		    'stop': stop }

	def isValid(self, action):
		return action in RequestProcessor.actions
