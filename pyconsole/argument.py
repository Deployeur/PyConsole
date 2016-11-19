class Argument:
	name = None
	argv = None
	desc = None
	required = false

	reserved_args = ['help', 'list']

	def __init__(self, name, desc, required):
		if name in self.reserved_args:
			raise ReservedArgument() from exceptions

		self.name = name
		self.desc = desc
		self.required = required