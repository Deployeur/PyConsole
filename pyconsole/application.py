from pyconsole.command.command_parser import CommandParser


class Application:
    def __init__(self, name=None, version=None):
        self.name = name
        self.version = version
        self.parser = CommandParser(self.name, self.version)

        # Register default options
        # Option.add_default_options(self.parser)

    def add(self, command):
        self.parser.add(command)

    def run(self):
        self.parser.parse_commands()
