from flask_restful import fields, marshal_with, request, Resource
from flask_restful_swagger import swagger

@swagger.model
class RequestModel:
	resource_fields = {
		'id': fields.String,
		'created': fields.DateTime,
		'status': fields.Boolean,
		'action': fields.String
	}


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
	@marshal_with(RequestModel.resource_fields)
	def get(self):
		pass #jsonify data

	@swagger.operation(
		notes='Adds a request to the server',
		nickname="Add request",
		parameters=[
		{
			'name': 'body',
			'description': 'request to be added',
			'required': True,
			'allowMultiple': True,
			'dataType': RequestModel.__name__,
			'paramType': 'body'
		}
		],
		responseMessages=[
			{
				'code': 201,
				'message': 'Request created'
			},
			{
				'code': 405,
				'message': 'Invalid request'
			}
		])
	@marshal_with(RequestModel.resource_fields)
	def post(self):
		req = request.get_json()
		print req


