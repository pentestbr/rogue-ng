from flask import Flask, jsonify
from flask_restful import Api
from flask_restful_swagger import swagger

from errors import errors
from resources import status, request
from server import Server

class RogueApi:

	resources = [{'handler': status.Status, 'path': '/api/status'},
		     {'handler': request.Request, 'path': '/api/requests'}]

	def __init__(self):
		self.server = Server()

	def run(self):
		self.app = Flask(__name__)
		self.api = swagger.docs(Api(self.app, errors=errors),
					  apiVersion='0.1',
					  api_spec_url='/api/rogue-ng')

		self.add_resources()


		self.app.run(debug=True, use_debugger=False, host="0.0.0.0")

	def add_resources(self):
		for resource in RogueApi.resources:
			self.api.add_resource(resource['handler'],
					      resource['path'],
					      resource_class_kwargs={'server':self.server})
