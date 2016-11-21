#!/usr/local/bin/python3
from commands.pull_command import PullCommand
from pyconsole.application import Application
from commands.open_chrome_command import OpenChromeCommand

# Init the application
application = Application('Testing CLI', '2.1')

# Add the commands
# application.add(OpenChromeCommand())
application.add(PullCommand())

# Run the app!
application.run()
