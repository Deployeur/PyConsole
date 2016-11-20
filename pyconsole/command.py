from pyconsole.argument import Argument
from pyconsole.option import Option


class Command:
    name = None
    desc = None
    argv = None
    opts = []

    def set_name(self, name):
        self.name = name
        return self

    def set_description(self, desc):
        self.desc = desc
        return self

    def add_argument(self, name, required=False, description=None):
        self.argv = Argument(name, description, required)
        return self

    def add_option(self, short_name, long_name, required=False, description=None):
        option = Option(short_name, long_name, description, required)
        self.opts.append(option)
        return self

    def get_options(self):
        options_list = {}

        for option in self.opts:
            options_list['-' + option.short_name] = '--' + option.long_name

        return options_list

    def parse_options(self, parser):
        for option in self.opts:
            parser.add_argument('-' + option.short_name, '--' + option.long_name, required=option.required, help=option.desc)
