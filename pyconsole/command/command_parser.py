import sys;
from pyconsole.command.command import Command
from pyconsole.input.input import Input
from pyconsole.output.output import Output


class CommandParser:
    app_name = None
    app_version = None
    executable_name = None
    input_args = None
    commands = []

    def __init__(self, app_name, app_version):
        self.app_name = app_name
        self.app_version = app_version
        self.executable_name = sys.argv[0:1][0]
        self.input_args = sys.argv[1:]

    def add(self, command: Command):
        self.commands.append(command)

    def parse_commands(self):
        argument_set = False

        if not self.input_args:
            title_length = (len(self.app_name) + len(self.app_version) + 1)

            Output.print(self.app_name + ' ' + self.app_version)
            Output.print(('-' * title_length)[:title_length])
            Output.print('~ Help here ~')
            return

        input = Input()

        for command in self.commands:
            command.configure()

            if not argument_set:
                argument = command.argv.name

                # Make sure the main argument is proper
                if argument == self.input_args[0]:
                    argument_set = True
                    del self.input_args[0]

                    # Does the argument need a value?
                    if command.argv.required:
                        if len(self.input_args) < 2:
                            Output.error(self.executable_name, 'Argument value missing.')
                        else:
                            input.add(argument, self.input_args[1])
                            del self.input_args[1]
                    # Try to use default instead
                    elif command.argv.default:
                        input.add(argument, command.argv.default)
                else:
                    Output.error(self.executable_name, 'Invalid argument [' + argument +'] provided.')

                # Fix up the options now...
                cleared_opts = [arg.replace('-', '') for arg in self.input_args]

                print(cleared_opts)

                for option in command.opts:
                    if option.short_name not in cleared_opts and option.long_name not in cleared_opts:
                        Output.error(self.executable_name, 'Invalid option [--' + option.long_name + '] provided.')
                    else:
                        pass
                        # if option.required
