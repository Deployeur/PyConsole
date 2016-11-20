from argparse import ArgumentParser
from pyconsole.command import Command
from pyconsole.option import Option


class Application:
    name = 'My CLI App'
    version = '1.0'
    commands = []
    arg_parser = None

    def __init__(self, name, version):
        self.name = name
        self.version = version
        self.arg_parser = ArgumentParser()

        # Register default options
        Option.add_default_options(parser=self.arg_parser)

    def add(self, command: Command):
        command.configure()
        self.commands.append(command)

    def run(self):
        self.arg_parser.add_argument('action', help="display a square of a given number")
        args = self.arg_parser.parse_args()

        print(args)
