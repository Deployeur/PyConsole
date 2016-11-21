# PyConsole

This package simplifies the process of creating scalable CLI apps. Simply create command classes, attach them to the application object and you're set! For a quick CLI app, simply add an anonymous function to the `add`method.

This package was inspired by Symfony's Console Component.

# Installation

Run this command and you're set:

```
$ pip3 install pyconsole
```

# Usage

Create a base file (we'll name it `exec.py` in this case) that will serve as the **executable** and then do the following:

```python
from pyconsole.application import Application
from commands.open_chrome_command import OpenChromeCommand  # Import your commands up here

# Init the application
application = Application('Testing CLI', '2.1')

# Add the commands
application.add(OpenChromeCommand())

# Run the app!
application.run()
```

And an example `command` class:

```python
from pyconsole.command import Command


class OpenChromeCommand(Command):
    def configure(self):
        self.set_name('Chrome Opener') \
            .set_description('Manage a Chrome window.') \
            .add_argument(name='open', description='Opens chrome up.') \
            .add_option(short_name='ff', long_name='fill_fields', description="Fill the page's input(s)")

    def execute(self, input, output):
        pass # Whatever logic needed to open a Chrome window and fill the fields in the page (hint: Selenium)...
```

And now execute the CLI app as follows:

```
python3 exec.py open google.com --fill_fields "Finding Dory"
```

That's it!

# Documentation

Coming soon...

# License

This package is released under the [MIT License](https://github.com/dugajean/PyConsole/blob/master/LICENSE).
