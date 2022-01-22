"""
The power of lambda is better shown when you use them as an anonymous function inside another function.

Say you have a function definition that takes one argument, and that argument 
will be multiplied with an unknown number:

"""

def myfunc(n):
  return lambda a : a * n


def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))