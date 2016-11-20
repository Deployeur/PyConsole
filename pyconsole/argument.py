from pyconsole.exceptions.reserved_argument import ReservedArgument


class Argument:
    name = None
    argv = None
    desc = None
    required = False

    # List of reserves arguments
    reserved_args = ['help', 'list']

    def __init__(self, name, desc, required):
        if name in self.reserved_args:
            raise ReservedArgument()

        self.name = name
        self.desc = desc
        self.required = required

    def get_name(self):
        return self.name

    def get_description(self):
        return self.desc
