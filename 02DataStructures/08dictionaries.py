"""A dictionary is a mutable data type that stores mappings of unique keys to values.
Here's a dictionary that stores elements and their atomic numbers.
stores in the following format : {key1:value1, key2:value2, key3:value3, key4:value4, ...} """

# is and is not are called identity operators 

elements = {"hydrogen" : 1, "helium" : 2, "carbon" : 6}
print(elements)           # prints all the keys and values
print(elements.keys())    # prints only keys
print(elements.values())  # prints onyl values

print("carbon" in elements)   # returns true as it is present in the dict 
print(6 in elements)          # returns false it will check only keys not values 
print(elements.get("helium")) # returns the value of the key, if key don't find the value then it returns None

elements["lithium"] = 3
print(elements) # the above key and value will be added to the dict 
print("carbon" in elements)
print("methene" in elements) #returns false

x = elements.get('dilithium')
is_null = x is None
print(is_null)        

n = elements.get("dilithium")
print(n is None)
print(n is not None)

