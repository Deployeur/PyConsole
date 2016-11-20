# PyConsole

This package simplifies the process of creating scalable CLI apps. Simply create command classes, attach them to the application object and you're set! For a quick CLI app, simply add an anonymous function to the `add`method.

## Installation

Run this command and you're set:

```
pip3 install pyconsole
```

## Usage

Create a base file that will serve as the executable and then do the following:

```

from pyconsole.application import Application
from commands.open_chrome_command import OpenChromeCommand  # Import your commands  # Import your commands  # Import your commands  # Import your commandsimport OpenChromeCommand

# Init the application
application = Application('Testing CLI', '2.1')

# Add the commands
application.add(OpenChromeCommand())

# Run the app!
application.run()
```
