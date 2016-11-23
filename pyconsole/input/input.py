class Input:
    def __init__(self, args={}):
        self.args = args

    def add(self, key, value):
        self.args[key] = value

    def get(self, key):
        return self.args[key]
