import httplib2
import json

from exceptions import RogueError

class ApiClient:

	def __init__(self, url):
		self.url = url
		self.http = httplib2.Http()

	def get(self, path):
		return self.http.request(self.url+path, 'GET')

	def putpost(self, path, content, type):
			return self.http.request(
				uri=self.url+path,
				method=type,
				headers={'Content-Type': 'application/json; charset=UTF-8'},
				body=json.dumps(content),
			)

	def put(self, path, content):
		return self.putpost(path, content, 'PUT')

	def post(self, path, content):
		return self.putpost(path, content, 'POST')


	def update_module_use(self, name, state):
		response, content = self.post('/modules/'+name,
					      {'name': name, 'used': state})
		if response.status == 200:
			return None
		elif response.status == 404:
			return 'Unknown module:', name
		else:
			print content
			raise RogueError('Unexpected response from server: '
					 + str(response.status))

	def load_module(self, name):
		return self.update_module_use(name, True)

	def remove_module(self, name):
		return self.update_module_use(name, False)

	def list_modules(self):
		response, content = self.get('/modules')
		return [mod['name'] for mod in json.loads(content)]

	def check_status(self):
		try:
			response, content = self.get('/status')
			return json.loads(content)
		except:
			return { 'status': 'down', 'enabled': 'unlikely' }

	def request(self, request):
		response, content = self.post('/requests', request)
		if response.status == 201:
			return json.loads(content)
		else:
			raise RogueError('Server responded to what should have been '
					 'a valid error with '+str(response.status))

	def request_start(self):
		self.request( { 'action': 'start' } )

	def request_stop(self):
		self.request( { 'action': 'stop' } )
