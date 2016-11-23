class Argument:
    def __init__(self, name, desc, required=False, default=False):
        self.name = name
        self.desc = desc
        self.required = required
        self.default = default
