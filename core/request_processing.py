import time

from threading import Lock, Thread


class RequestProcessor:



	def __init__(self):
		self.sleep_between_requests = 0.2
		self.requests = []
		self.lock = Lock()

	def start(self):
		self.worker = Thread(target=self.run)
		self.running = True
		self.worker.start()

	def stop(self):
		self.running = False

	actions = { 'start': start,
		    'stop': stop }

	def isValid(self, action):
		return action in RequestProcessor.actions

	def add_request(self, request):
		self.lock.acquire()
		self.requests.append(request)
		self.lock.release()

	def run(self):
		print 'Request Processor started'
		while self.running:
			self.lock.acquire()
			if self.requests:
				process_a_request()
				self.lock.release()
			else:
				self.lock.release()
				time.sleep(self.sleep_between_requests)


	def process_a_request(self):
		self.lock.acquire()
		print 'Processing request:'
		self.lock.release()
