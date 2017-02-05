from flask import Flask, jsonify
from flask_restful import Api
from flask_restful_swagger import swagger

from resources import Status

class RogueApi:
	def run(self):
		self.app = Flask(__name__)
		self.api = swagger.docs(Api(self.app), apiVersion="0.1")

		self.add_resources()


		self.app.run(debug=True, host="0.0.0.0")

	def add_resources(self):
		self.api.add_resource(Status, "/api/status")

