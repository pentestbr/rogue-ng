#!/usr/bin/python

from flask import Flask

app = Flask(__name__)


@app.route('/rogue-ng/api/v1.0/status', methods=['GET'])
def get_status():
	return 'Up and running capt\'n'



if __name__ == '__main__':
	app.run(debug=True)

