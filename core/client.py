import httplib2
import json

class ApiClient:

	def __init__(self, url):
		self.url = url
		self.http = httplib2.Http()

	def get(self, path):
		return self.http.request(self.url+path, 'GET')

	def port(self, path, content):
		return self.http.request(self.url+path, 'POST', content)

	def check_status(self):
		try:
			response, content = self.get('/status')
			return json.loads(content)
		except:
			return { 'status': 'down', 'enabled': 'unlikely' }

	def request_start(self):
		pass

	def request_stop(self):
		pass
