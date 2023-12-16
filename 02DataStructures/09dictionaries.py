# TODO: replace None with appropriate code
# Define a dictionary, `population`, that provides information
# on the world's largest cities. The key is the name of a city
# (a string), and the associated value is its population in
# millions of people.
#   Key     |   Value
# Shanghai  |   17.8
# Istanbul  |   13.3
# Karachi   |   13.0
# Mumbai    |   12.5

population = {"Shanghai":17.8, "Istanbul":13.3, "Karachi":13.0, "Mumbai":12.5}
print(population)



a = [1, 2, 3]  # Create a list 'a' with elements 1, 2, and 3
b = a          # Assign the reference of list 'a' to list 'b'
c = [1, 2, 3]  # Create a new list 'c' with the same elements as list 'a'
print(a == b)  # Check if the elements of lists 'a' and 'b' are equal # Output: True
print(a is b)  # Check if lists 'a' and 'b' reference the same object in memory # Output: True
print(a == c)  # Check if the elements of lists 'a' and 'c' are equal # Output: True
print(a is c)  # Check if lists 'a' and 'c' reference the same object in memory # Output: False