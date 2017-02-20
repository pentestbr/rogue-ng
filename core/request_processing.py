import time

from threading import Lock, Thread


class RequestProcessor:

	def __init__(self):
		self.sleep_between_requests = 10
		self.requests = []
		self.lock = Lock()
		self.next_id = 1

	def start(self):
		self.worker = Thread(target=self.run)
		self.worker.daemon = True
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
		request['id'] = self.next_id
		self.next_id += 1
		self.requests.append(request)
		self.lock.release()

	def run(self):
		print 'Request Processor started'
		while self.running:
			if self.requests:
				self.process_a_request()
			else:
				print "sleeping.."
				time.sleep(self.sleep_between_requests)


	def process_a_request(self):
		self.lock.acquire()
		request = self.requests.pop(0)
		print 'Processing request:', request

		self.lock.release()
