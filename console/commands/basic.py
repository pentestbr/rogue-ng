import sys

class Help:
	def execute(self):
		print 'recon-ng 2017'
		print 'Useful commands:'
		print '\thelp        Pretty frickin obvious. You typed it to get here'

class Quit:
	def execute(self):
		sys.exit()
