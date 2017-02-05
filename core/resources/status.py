from flask_restful import Resource
from flask_restful_swagger import swagger

class Status(Resource):

	@swagger.operation()
	def get(self):
		return {'status':'live'}
