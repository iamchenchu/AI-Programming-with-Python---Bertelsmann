"""Scripting with Raw Input
We can get raw input from the user with the built-in function input, which takes in an optional string argument that you can use to specify a message to show 
to the user when asking for input."""

name = input('Enter a name :')
age = input('Enter your age :')

print("Hello", name.title())
print("Your age is :", age)

result = eval(input("enter your expression : "))
print(result)