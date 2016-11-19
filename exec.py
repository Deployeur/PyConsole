#!/usr/bin/python

from pyconsole.application import Application

# Init the application
application = Application('Testing CLI', '2.1')

# Add the commands
application.add('strtest')

# Run the app!
application.run()