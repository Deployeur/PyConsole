#!/usr/local/bin/python3

from pyconsole.application import Application
from commands.open_chrome_command import OpenChromeCommand

# Init the application
application = Application('Testing CLI', '2.1')

# Add the commands
application.add(OpenChromeCommand())

# Run the app!
application.run()