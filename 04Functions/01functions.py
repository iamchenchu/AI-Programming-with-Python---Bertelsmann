"""Welcome to this lesson on Functions! Functions are useful blocks of code that allow you to encapsulate a task. Encapsulation allows us to carry out a whole series of steps 
with one simple command. You can think about functions as a way to take what you have already learned how to do and put it in an easy-to-use container that allows you to 
use it over and over again.
In the diagram below, the container represents the function, the circle above it represents any input you may need to feed into the function, and 
the circle below represents any output you may get out of the function. In the example of the bake_cake function, you may want to provide the ingredients and prepare your
baking pans as inputs, then bake_cake with those baking pans. You will get a cake as an output."""

#In this lesson, you will learn about:
"""
1.Defining Functions
2.Variable Scope
3.Documentation
4.Lambda Expressions
5.Iterators and Generators"""

#Let's write our first function which of a volume of a cylinder

def cylinder_volume(height, radius):                
    pi = 3.14159
    return height * pi * radius ** 2

print(cylinder_volume(10, 3))
print(cylinder_volume(height=10, radius=7))  # pass in arguments by name



"""Function Header
Let's start with the function header, which is the first line of a function definition.

The function header always starts with the def keyword, which indicates that this is a function definition.
Then comes the function name (here, cylinder_volume), which follows the same naming conventions as variables. You can revisit the naming conventions below.
Immediately after the name are parentheses that may include arguments separated by commas (here, height and radius). Arguments, or parameters, are values that are passed in as inputs when the function is called, and are used in the function body. If a function doesn't take arguments, these parentheses are left empty.
The header always end with a colon :."""

"""Function Body
The rest of the function is contained in the body, which is where the function does its work.
The body of a function is the code indented after the header line. Here, it's the two lines that define pi and return the volume.
Within this body, we can refer to the argument variables and define new variables, which can only be used within these indented lines.
The body will often include a return statement, which is used to send back an output value from the function to the statement that called the function. 
A return statement consists of the return keyword followed by an expression that is evaluated to get the output value for the function. If there is no return statement, 
the function simply returns None."""