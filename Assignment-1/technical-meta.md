# Meta

## Hosting
The systems should use FastAPI for its API(s) and be hosted on Render. (Note that much of the development can be done locally.)

You should be using a database for storing the dataset during while running. You decide which kind of database fits you — or this project — best.


## Programming environment
The system/subsystems should be written in Python.

It should be tested using pytest, flake8 and mypy. Include good-ish unit tests for helper functions.

It should include some API endpoint tests as well, in another script. This does not have to be very complex, but should do some basic stuff, like cheching that adding and consuming tokens actually affect the tokens.
Use would be something like: Launch API, wait a bit and then run test script. Tests passed = all good.


## Coding style
Follow PEP 8 style guides, that is, make sure flake8 approves of your code. Feel free to ignore rules when you find it needed.

Don't write functions with 100 lines of code. Don't include 


## Documentation
The code should include docstrings for files, classes (if used) and functions/methods.
They do not have to follow standardized docstring formats, but should be relatively consistent throughout the project.
