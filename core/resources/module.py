from flask_restful import inputs, fields, marshal_with, abort, reqparse, request 
from flask_restful import Resource 
from flask_restful_swagger import swagger

@swagger.model
class ModuleModel:
        resource_fields = {
                'name': fields.String,
		'used': fields.Boolean,
                'config': fields.String
        }

class ModuleList(Resource):
        def __init__(self, **kwargs):
                self.server = kwargs['server']

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

class Module(Resource):

	def __init__(self, **kwargs):
		self.server = kwargs['server']
		self.create_parser = reqparse.RequestParser()
		self.create_parser.add_argument('name', 
						help='Required field', 
						required=True)
		self.create_parser.add_argument('config')
		self.create_parser.add_argument('used', type=inputs.boolean)

	@swagger.operation(
		notes='Retrieves a specific module',
		nickname='Get Module',
		responseClass=ModuleModel.__name__,
		responseMessages=[
			{
				'code': 200,
				'message': 'Module retrived'
			},
			{
				'code': 404,
				'message': 'Module with that name not found'
			}
		]
	)
	@marshal_with(ModuleModel.resource_fields)
	def get(self, name):
		if name in self.server.modules:
			module = self.server.modules[name]
			return module, 200
		else:
			abort(404, message='Module {} does not exist'.format(name))

	@swagger.operation(
		notes='Updates a module, most commonly to set to be used or configured',
		nickname='Update module',
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
				'code': 200,
				'message': 'Module updated'
			},
			{
				'code': 404,
				'message': 'Unknown module'
			},
			{
				'code': 400,
				'message': 'Invalid config'
			}
		])
	@marshal_with(ModuleModel.resource_fields)
	def post(self, name):
		args = self.create_parser.parse_args()
		name = args['name']
		config = args['config']
		used = args['used']
		return self.server.update_module(name, config, used), 200
