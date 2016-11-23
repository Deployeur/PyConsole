from pyconsole.command.command import Command


class OpenChromeCommand(Command):
    def configure(self):
        self.set_name('Chrome Opener') \
            .set_description('Manipulate a Chrome window.') \
            .add_argument(name='test', required=False, description='Opens chrome up.') \
            .add_option(short_name='gt', long_name='goto', description='Which page should we go to...')

    def execute(self, input, output):
        goto_arg = input.get('goto')
