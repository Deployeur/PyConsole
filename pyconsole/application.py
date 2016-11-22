from pyconsole.command.command_parser import CommandParser
from pyconsole.input.input import Input
from pyconsole.input.input_option import Option
from pyconsole.output.output import Output


class Application:
    name = 'My First Application'
    version = '0.1'
    parser = None

    def __init__(self, name=None, version=None):
        self.name = name
        self.version = version
        self.parser = CommandParser()

        # Register default options
        # Option.add_default_options(self.parser)

    def add(self, command):
        command.configure()
        self.parser.add(command)

    def run(self):
        pass
        # input = Input()
        # output = Output(input)

        # for command in self.commands:
        #     command.execute(input, output)
