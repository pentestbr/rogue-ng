from werkzeug.exceptions import HTTPException

class InvalidActionException(HTTPException):
	code = 405

class RogueError(Exception):
	pass

class UnknownModule(HTTPException):
	pass
