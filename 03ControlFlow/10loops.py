"""Python have 2 type of loops which are for and while
For loop : we can iterate on iterable. An iterable is an object that can return one of its elements at a time.
This can include sequence types, such as strings, lists, and tuples, as well as non-sequence types, such as dictionaries and files """

cities = ['New York', 'mountain view', 'chicago', 'los angeles']

for city in cities:                    # for signals that it is as for loop
    print(city.title())                # cities is iterable and city is iteration variable

# we use title()
print(" ")
print("the belwo part is in another way to print the same as index wise")
print(" ")

for index in range(len(cities)):
    print(cities[index].upper())
