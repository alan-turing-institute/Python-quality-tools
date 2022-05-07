"""
A few examples of errors and style checks picked up by pylint but not by flake8 or
mypy. The pylint documentation has a list of all messages:
https://pylint.pycqa.org/en/latest/messages/messages_list.html#messages-list

The first letter of the code relates to the category of problem: (C)onvention,
(E)rror, (F)atal, (I)nformation, (R)efactor, (W)arning
"""

# C0103 (invalid-name)
# Variable detected as being a constant, which should be upper case by convention
aaa = 24


# C0116 (missing-function-docstring)
# Functions should have docstrings
def cool_function():
    return "icy"


# W0102 (dangerous-default-value)
# Mutable default arguments may have unexpected effects, see
# https://stackoverflow.com/a/26320938/12336896
def update(data={}):
    """Update the data"""
    data.update({"key": "value"})
    return data


# E0213 (no-self-argument)
# First argument of class function isn't self
# R0903 (Too few public methods)
# Class that has fewer than 2 public methods
class Dragon:
    """Big green lizardy thing"""

    def __init__(some):
        pass


# R0913 (too-many-arguments)
# By default, pylint will flag functions with more than 5 arguments
def many_args(thing1, thing2, thing3, thing4, thing5, thing6, thing7, thing8):
    """Add some things"""
    return thing1 + thing2 + thing3 + thing4 + thing5 + thing6 + thing7 + thing8


# R1703 (simplifiable-if-statement)
def taller(my_height: int, your_height: int) -> bool:
    """Am I taller than you?"""
    if my_height > your_height:
        me_taller = True
    else:
        me_taller = False

    return me_taller
