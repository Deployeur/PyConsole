import sys;

class Output:
    @staticmethod
    def print(message, before=''):
        print((before + ': ' if before else '') + message)

    @staticmethod
    def error(executable, message):
        Output.print(before=executable, message=message)
        Output.print(before='Usage', message=executable + ' [argument] [--options]')
        sys.exit(2)
