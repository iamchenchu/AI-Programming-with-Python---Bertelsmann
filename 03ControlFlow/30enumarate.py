# Many time you will find it useful to iterate through the values of a list, along with the index then
# below way is one of doing it using for loop
"""Enumerate: 
enumerate is a built in function that returns an iterator of tuples containing indices and values of a list. 
You'll often use this when you want the index along with each element of an iterable in a loop."""

items = ['bananas', 'mattresses','dog kennels','machine','cheeses']

for i, item in zip(range(len(items)), items):
    print(i, item)
    dict1 =dict(enumerate(items, start=1)) #Creating a dictionary from the indices and items
print(dict1)

print("       ")
print("*********************")
print("       ")
print("below is the another example for enumarate")
letters = ['a', 'b', 'c', 'd', 'e']
for i, letter in enumerate(letters):
    print(i, letter)
