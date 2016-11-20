from pyconsole.exceptions.reserved_option import ReservedOption


class Option:
    short_name = None
    long_name = None
    desc = None
    required = False

    # List of reserved options
    reserved_opts = {'v': 'verbose', 'n': 'no-interaction'}

    def __init__(self, short_name, long_name, desc, required):
        if long_name in self.reserved_opts.values() or short_name in self.reserved_opts:
            raise ReservedOption()

        self.short_name = short_name
        self.long_name = long_name
        self.desc = desc
        self.required = required

    def get_short_name(self):
        return self.short_name

    def get_long_name(self):
        return self.long_name

    def get_description(self):
        return self.desc

    def get_required(self):
        return self.required

    @staticmethod
    def add_default_options(parser):
        group = parser.add_mutually_exclusive_group()
        for short, long in Option.reserved_opts.items():
            group.add_argument('-' + short, '--' + long, action='store_true')