import readline

class RogueCompleter:

	no_match_text = ['Foobar']

	def __init__(self, _cmds):
		self.cmds = _cmds

	def complete_cmd(self, text):
		return  [ x for x in self.cmds.keys() if x.startswith(text) ]

	def complete(self, text, state):
		line = self.get_line_before()
		if len(line) == 0: matches = self.complete_cmd(text)
		else: matches = self.get_sub_matches(line, text)

		try:
			return matches[state]
		except IndexError:
			return None

	def get_line_before(self):
		idx = readline.get_begidx()
		full = readline.get_line_buffer()
		return full[:idx].split()

	def get_sub_matches(self, line, text):
		cmd = line[0]
		if cmd in self.cmds: return self.cmds[cmd].complete(line, text)
		else: return RogueCompleter.no_match_text
