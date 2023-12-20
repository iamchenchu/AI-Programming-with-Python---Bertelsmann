"""zip and enumerate are useful built-in functions that can come in handy when dealing with loops"""

letters = ['a', 'b', 'c']
nums = [1, 2, 3]

for letter, num in zip(letters, nums):
    print("{} : {}".format(letter, num))
    dict1 = dict(zip(letters, nums))
print(dict1)


