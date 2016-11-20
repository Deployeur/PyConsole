from pyconsole.argument import Argument
from pyconsole.option import Option


class Command:
    name = None
    desc = None
    args = []
    opts = []

    def set_name(self, name):
        self.name = name
        return self

    def set_description(self, desc):
        self.desc = desc
        return self

    def add_argument(self, name, required=False, description=None):
        self.args.append(Argument(name, description, required))
        return self

    def add_option(self, name, argv, required=False, description=None):
        option = Option(name, argv, description, required)
        self.opts.append(option)
        return self

    def get_options(self):
        options_list = []

        for option in self.opts:
            options_list.append(option.get_name() + ('=' if option.get_required() else ''))

        return options_list
