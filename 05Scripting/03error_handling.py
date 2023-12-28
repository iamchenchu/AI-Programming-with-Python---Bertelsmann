"""Errors and Exceptions
Syntax errors occur when Python can’t interpret our code, since we didn’t follow the correct syntax for Python. These are errors you’re likely to get when you make a typo, 
or you’re first starting to learn Python.
Exceptions occur when unexpected things happen during execution of a program, even if the code is syntactically correct. There are different types of built-in exceptions 
in Python, and you can see which exception is thrown in the error message."""

# Built-in Exception  :  An object of the correct type but inappropriate value is passed as input to a built-in operation or function.
# AssertionError   : An assert statement fails.
# IndexError :  A sequence subscript is out of range.
# KeyError : A key can't be found in a dictionary.
# TypeError : An object of an unsupported type is passed as input to an operation or function.

# Example of Syntax Error

# missing a closing quotation mark here which is causing the sysntax error
msg = "I am chenchu reddy
print(msg)



#Example of the Exception which is syntactically correct but causing exception 
num = 10

print(num)
print(num1)  # this is syntactically correct but we did not define the value for num1 which is causing the error.