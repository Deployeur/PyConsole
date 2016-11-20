from pyconsole.exceptions.reserved_argument import ReservedArgument


class Argument:
    name = None
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
