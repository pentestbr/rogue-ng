"A set of custom errors for the rest interface to use when exceptons are encountered"

errors = {
	'InvalidActionException': {
		'message': 'Server request asks for an invalid action to be performed',
		'status': 405
	},
	'UnknownModule': {
		'message': 'Invalid module',
		'status': 404
	}
}
