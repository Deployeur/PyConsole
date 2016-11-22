import sys;
from pyconsole.command.command import Command


class CommandParser:
    app_name = None
    input_args = None
    commands = []

    def __init__(self):
        self.app_name = sys.argv[0:1][0]
        self.input_args = sys.argv[1:]

        print(self.app_name, self.input_args)

    def add(self, command: Command):
        self.commands.append(command)

