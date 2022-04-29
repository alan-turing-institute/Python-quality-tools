# Blank line rules
#
# - Two blank lines between top level function/class definitions
# - One blank line between methods
# - No more than one blank line otherwise
#
# See https://peps.python.org/pep-0008/#blank-lines


def double(x: int) -> int:
    return 2*x


def triple(x: int) -> int:
    return 3*x


def quadruple(x: int) -> int:
    return 4*x


class Animal:
    ...


class Dog(Animal):
    def __init__(self) -> None:
        self.wagging = False

    def bark(self) -> str:
        return "BARK!"

    def wag(self) -> None:
        self.wagging = True
