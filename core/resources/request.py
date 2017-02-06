from flask_restful import Resource
from flask_restful_swagger import swagger

class Request(Resource):

	def __init__(self, **kwargs):
		self.server = kwargs['server']

	@swagger.operation(
		notes='Lists current requests for the server',
		nickname='Server Requests',
		responseMessages=[
			{
				'code': 200,
				'message': 'Server has returned a list of requests'
			},
			{
				'code': 404,
				'message': 'There are no requests to get'
			}
		])
	def get(self):
		pass
