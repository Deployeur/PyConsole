class Option:
	name = None
	argv = None
	desc = None
	required = false

	reserved_opts = ['-v', '-n']

	def __init__(self, name, argv, desc, required):
		if argv in self.reserved_opts:
			raise ReservedOption() from exceptions

		self.name = name
		self.argv = argv
		self.desc = desc
		self.required = required