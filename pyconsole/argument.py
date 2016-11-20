class Argument:
    name = None
    desc = None
    required = False

    def __init__(self, name, desc, required):
        self.name = name
        self.desc = desc
        self.required = required
