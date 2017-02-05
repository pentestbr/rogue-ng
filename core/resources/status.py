from flask_restful import Resource
from flask_restful_swagger import swagger

class Status(Resource):

	@swagger.operation(
		notes='A quick and easy test of whether the core server is live',
		nickname='Server Status',
		responseMessages=[
			{
				"code": 200,
				"message": "Server is live"
			}
		]
		)
	def get(self):
		return {'status':'live'}
