from werkzeug.exceptions import HTTPException

class InvalidActionException(HTTPException):
	code = 405
