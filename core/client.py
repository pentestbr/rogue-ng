import httplib2
import json

class ApiClient:

	def __init__(self, url):
		self.url = url
		self.http = httplib2.Http()

	def get(self, path):
		return self.http.request(self.url+path, 'GET')

	def check_status(self):
		try:
			response, content = self.get('/status')
			return json.loads(content)
		except:
			return { 'status': 'down', 'enabled': 'unlikely' }
