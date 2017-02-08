class RequestProcessor:

	def start(self):
		pass

	actions = { 'start': start }

	def isValid(self, action):
		return action in RequestProcessor.actions
