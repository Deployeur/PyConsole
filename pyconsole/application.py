import sys
from argparse import ArgumentParser
from pyconsole.command import Command
from pyconsole.option import Option


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

    def add(self, command: Command):
        command.configure()
        self.commands.append(command)

    def commands_list(self):
        commands_list = []

        for command in self.commands:
            commands_list.append(command.argv.name)

        return commands_list

    def run(self):
        self.arg_parser.add_argument('action', metavar='action', choices=self.commands_list())
        self.arg_parser.add_argument('value')
        args = vars(self.arg_parser.parse_args())

        for argument, value in args.items():
            print(argument, value)

    def parse_options(self):
        pass
