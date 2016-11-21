from pyconsole.option import Option


class Input:
    args = None

    def __init__(self, args):
        self.args = args
        self.cleanup()
        self.set_action()

    def set_action(self):
        self.args[self.args['action']] = self.args['value']
        del self.args['action'], self.args['value']

    def cleanup(self):
        for k in list(self.args.keys()):
            if k in Option.reserved_opts.values():
                del self.args[k]

    def get(self, key):
        return self.args[key]
