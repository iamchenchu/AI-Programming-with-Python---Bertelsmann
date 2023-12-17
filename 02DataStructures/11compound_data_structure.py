"""Compound Data Structures
We can include containers in other containers to create compound data structures. 
For example, this dictionary maps keys to values that are also dictionaries!"""
# Nested Dictionary is compound dictionary 

elements = {"hydrogen" :{"number":1,
                         "weight":1.00794,
                         "symbol":"H"},
            "helium" : {"number":2,
                        "weight":4.002602,
                        "symbol":"He"}}

print(elements["helium"])
print(elements["hydrogen"]["weight"])

oxygen = {"number" : 8, "weight": 15.999, "symbol": "O"}
elements["oxygen"] = oxygen
print(elements)

