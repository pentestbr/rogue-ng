import subprocess

class Module:

	#-------------------------------------
	# Interface
	#

	def __init__(self):
		self.services = []
		self.start_scripts = []
		self.stop_scripts = []
		self.running_scripts = []
		self.running_services = []

	def start(self):
		self.start_services()
		self.start_scripts()

	def stop(self):
		self.stop_services()
		self.stop_scripts()


	#-------------------------------------
	# Util methods
	#

	def start_services(self):
		for service in self.services:
			p = subprocess.Popen(['service', service, 'start')

	def stop_services(self):
		pass

	def start_scripts(self):
		pass

	def stop_scripts(self):
		pass
