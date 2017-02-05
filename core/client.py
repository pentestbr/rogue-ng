import httplib2

class ApiClient:

	def __init__(self, url):
		self.url = url
		self.http = httplib2.Http()

	def get(self, path):
		return self.http.request(self.url+path, 'GET')

	def check_status(self):
		try:
			response, content = self.get('/status')
			if response['status'] == '200':
				return True
			else:
				return False
		except:
			return False
