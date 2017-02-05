from flask import Flask
from flask_restful import Api

from resources import Status

class RogueApi:
	def run(self):
		app = Flask(__name__)
		api = Api(app)

		self.add_resources(api)

		app.run(debug=True)

	def add_resources(self, api):
		api.add_resource(Status, "/rogue-ng/api/status")

