class Command:
	name = None
	desc = None
	args = []
	opts = []

	def set_name(self, name):
		self.name = name

	def set_description(self, desc):
		self.desc = desc

	def add_argument(self, name, required = False, description = None):
		args.append(Argument(name, desc, required))

	def add_option(self, name, argv, required = False, description = None):
		args.append(Option(name, argv, desc, required))



		