"""You can use lambda expressions to create anonymous functions. That is, functions that don’t have a name. They are helpful for creating quick functions that aren’t needed 
later in your code. This can be especially useful for higher order functions, or functions that take in other functions as arguments."""

def multiply(x, y):
    return x * y

print(multiply(3,4))

#now see the same expression with lambda

multiplication = lambda x,y:x*y
print(multiplication(4,5))
