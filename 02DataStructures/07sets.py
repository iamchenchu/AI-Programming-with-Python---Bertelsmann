# Set is a data type for mutable and unordered collection of unique elements. 
# One application of a set is quickly remove the duplicates from list.
# We use add() to add the new element to the list, pop() used to remove the elements

numbers = (1, 2, 6, 3, 1, 1, 6) # it will not print the 1 for multiple times
unique_nums = set(numbers)
print(unique_nums)
unique_nums = unique_nums.add(10)
print(unique_nums)


fruit = {"apple", "banana", "orange", "grapefruit"}  # define a set
print("watermelon" in fruit)  # check for element

fruit.add("watermelon")  # add an element
print(fruit)
print(fruit.pop())  # remove a random element
print(fruit)

a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
b = set(a)
print(len(a) - len(b))
b.add(5)
print(b) # 5 element will be added to the set 
b.pop()
print(b) # random element would be deleted


