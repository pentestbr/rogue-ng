from flask_restful import fields, marshal_with, reqparse, request, Resource 
from flask_restful_swagger import swagger

@swagger.model
class ModuleModel:
        resource_fields = {
                'name': fields.String,
                'config': fields.String,
        }

class Module(Resource):
        def __init__(self, **kwargs):
                self.server = kwargs['server']
		self.create_parser = reqparse.RequestParser()
		self.create_parser.add_argument('name', 
						help='Required field', 
						required=True)
		self.create_parser.add_argument('config')

        @swagger.operation(
                notes='Lists the current modules',
                nickname='List Modules',
                responseClass=ModuleModel.__name__,
                responseMessages=[
                        {
                                'code': 200,
                                'message': 'Server has returned a list of modules'
                        }
		])
	@marshal_with(ModuleModel.resource_fields)
	def get(self):
		return self.server.get_modules()

	@swagger.operation(
		notes='Adds a module to the list of current running modules',
		nickname='Add module',
		parameters=[
		{
			'name': 'body',
			'description': 'name and config for module',
			'required': True,
			'allowMultiple': True,
			'dataType': ModuleModel.__name__,
			'paramType': 'body'
		}
		],
		responseMessages=[
			{
				'code': 201,
				'message': 'Module added'
			},
			{
				'code': 400,
				'message': 'Unknown module, or invalid config'
			}
		])
	@marshal_with(ModuleModel.resource_fields)
	def post(self):
		args = self.create_parser.parse_args()
		name = args['name']
		config = args['config']
		return self.server.add_module(name, config), 201
