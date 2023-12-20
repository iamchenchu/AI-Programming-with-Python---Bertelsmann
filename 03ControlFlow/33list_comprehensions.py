#Below is the example for square of a number 

squares = []
for x in range(9):
    squares.append(x**2)
print(squares)

#The above code is using the for loop
# Now let's see how it can be written suing the list comprehensions
sq1 = [x**2 for x in range(9)]
print(sq1)

# we can also add the conditions if required in our list comprehensions
sqr = [x**2 for x in range(9) if x%2 == 0]
print(sqr)

#if you want to add the else statement then u have to get the condition to the begining of the statement as below 
sqr1 = [x**2 if x%2 == 0 else x+3 for x in range(9)]
print(sqr1)