cast = {"Jerry Seinfeld" : "Jerry Seinfeld",
        "Julia Louis-Dreyfus" : "Elaine Benes",
        "Jason Alexander" : "George Costanza",
        "Michael Richards" : "Cosmo Kramer"
        }

for key in cast:
    print(key)     # Prints all the keys in cast dictionary

for value in cast:
    print(value)  # Prints all the values in cast dictionary

# We can also iterate through both keys and values, you can use built in method items() as below 
    
for key, value in cast.items():
    print("Actor : {}    Role : {}".format(key, value))
    