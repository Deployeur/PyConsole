from pyconsole.exceptions.reserved_option import ReservedOption


class Option:
    short_name = None
    long_name = None
    desc = None
    required = False
    default = False

    # List of reserved options
    reserved_opts = {'v': 'verbose', 'n': 'no_interaction'}

    def __init__(self, short_name, long_name, desc, required=False, default=False):
        if long_name in self.reserved_opts.values() or short_name in self.reserved_opts:
            raise ReservedOption()

        self.short_name = short_name
        self.long_name = long_name
        self.desc = desc
        self.required = required
        self.default = default

    @staticmethod
    def add_default_options(parser):
        group = parser.add_mutually_exclusive_group()
        for short, long in Option.reserved_opts.items():
            group.add_argument('-' + short, '--' + long, action='store_true')