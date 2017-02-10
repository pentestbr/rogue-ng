class RogueCompleter:

	def __init__(self, _cmds):
		self.cmds = _cmds

	def complete(self, text, state):
		matches = [ x for x in self.cmds if x.startswith(text) ]
		try:
			return matches[state]
		except IndexError:
			return None
