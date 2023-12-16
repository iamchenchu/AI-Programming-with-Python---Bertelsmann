list_of_random_things = [1, 3.4, 'a string', True]
print(list_of_random_things)
print(list_of_random_things[-1])
print(list_of_random_things[1:]) #prints all the elements post 1st index 


months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
q3 = months[6:9]
print(q3)
first_half = months[:6]
print(first_half)
print(len(months))
print(len(months[1])) # prints the element length in the list 

 #KEY WORDS in AND not in 
# in keyword (evaluates if the object on left side is included in object on right side)
# not in evaluates if the object on the lest side is not included in  object on the right side 

print("sunday" in months)
print("jun" not in months)
print("jan" in months)


