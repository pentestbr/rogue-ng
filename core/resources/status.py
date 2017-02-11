from flask_restful import Resource
from flask_restful_swagger import swagger

class Status(Resource):

	def __init__(self, **kwargs):
		self.server = kwargs['server']

	@swagger.operation(
		notes='Gets the current server status',
		nickname='Server Status',
		responseMessages=[
			{
				"code": 200,
				"message": "Server is live"
			}
		]
		)
	def get(self):
		modules = [ x['name'] for x in self.server.modules.values() if x['used']]
		return {'status': 'Live',
			'enabled': self.server.enabled,
			'modules': modules}
