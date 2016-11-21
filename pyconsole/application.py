from argparse import ArgumentParser
from pyconsole.input.input import Input
from pyconsole.input.input_option import Option
from pyconsole.output.output import Output


class Application:
    name = 'My CLI App'
    version = '1.0'
    commands = []
    arg_parser = None

    def __init__(self, name=None, version=None):
        self.name = name
        self.version = version
        self.arg_parser = ArgumentParser(description=self.name + ' ' + self.version)

        # Register default options
        Option.add_default_options(self.arg_parser)

    def add(self, command):
        command.configure()
        self.commands.append(command)

    def commands_list(self):
        commands_list = []

        for command in self.commands:
            commands_list.append(command.argv.name)

        return commands_list

    def set_options(self):
        self.commands[0].parse_options(self.arg_parser)

    def run(self):
        self.arg_parser.add_argument('action', metavar='action', choices=self.commands_list())
        self.arg_parser.add_argument('value', default=None)
        self.set_options()

        input = Input(vars(self.arg_parser.parse_args())).args
        output = Output(input)

        for command in self.commands:
            command.execute(input, output)
