from pyconsole.command import Command

class OpenChromeCommand(Command):
	def configure(self):
		self.set_name('Chrome Opener').set_description('Manipulate a Chrome window.').add_argument(name='help', required=True, description='Opens chrome up.').add_option(name='goto', argv='--goto', required=True, description='Which page should we go to...')

	def execute(self, input, output):
		pass
		