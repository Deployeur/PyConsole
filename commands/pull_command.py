from pyconsole.command.command import Command


class PullCommand(Command):
    def configure(self):
        self.set_name('Pull from Github') \
            .set_description('Perform a pull nice and well.') \
            .add_argument(name='pull', required=True, description='Performs the pull.') \
            .add_option(short_name='r', long_name='remote', description='Where to pull from?')

    def execute(self, input, output):
        print(input)

