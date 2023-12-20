"""zip and enumerate are useful built-in functions that can come in handy when dealing with loops"""
# ZIP returns an iterator that combines multiple iterables into one sequence of tuples. Each tuple contains the elemets in that position 
# from all the iterables

#Below one is to zip the 2 data structures together into a dictionary
letters = ['a', 'b', 'c']
nums = [1, 2, 3]

for letter, num in zip(letters, nums):
    print("{} : {}".format(letter, num))
    dict1 = dict(zip(letters, nums))
    list1 = list(zip(letters, nums))
print(dict1)
print(list1)

print("*********")
print("     ")
print("Below one is to unzip the dict into 2 data structures")
print("Now we know that the dict1 is a dictionary which we created the above")
l,n = zip(*dict1.items())
print(l)
print(n)