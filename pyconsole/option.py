from pyconsole.exceptions.reserved_option import ReservedOption


class Option:
    name = None
    argv = None
    desc = None
    required = False

    # List of reserves options
    reserved_opts = ['verbose', 'no-interaction']

    def __init__(self, name, argv, desc, required):
        if argv in self.reserved_opts:
            raise ReservedOption()

        self.name = name
        self.argv = argv
        self.desc = desc
        self.required = required

    def get_name(self):
        return self.name

    def get_description(self):
        return self.desc

    def get_required(self):
        return self.required
