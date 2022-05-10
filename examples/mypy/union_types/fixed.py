# Union types and type inference
# a is infered to by of type `int`. We then try to assign a literal string to a
a: int | str = 1
a = 'hello'

# or

a = 1
a_str = 'hello'
