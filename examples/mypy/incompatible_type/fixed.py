# Incompatible type for a function argument
# Adapted from the mypy documentation
# https://mypy.readthedocs.io/en/latest/getting_started.html#function-signatures-and-dynamic-vs-static-typing
#
# Note that both calls of greeting would result in runtime errors as the str
# __add__ method raises TypeError if the argument type is not str.

def greeting(name: str) -> str:
    return 'Hello ' + name


greeting(str(3))
greeting(b'Alice'.decode())
