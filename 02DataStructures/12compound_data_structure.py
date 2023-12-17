"""elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}
# TODO: Add an 'is_noble_gas' entry to the hydrogen and helium dictionaries
elements["hydrogen"]["is_noble_gas"] : False
elements["helium"]["is_noble_gas"] : True
print(elements['hydrogen'])
"""


elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}

# Add 'is_noble_gas' entry to the dictionaries
elements['hydrogen']['is_noble_gas'] = False
elements['helium']['is_noble_gas'] = True

# Test the lookups
print(elements['hydrogen']['is_noble_gas'])  # Output: False
print(elements['helium']['is_noble_gas'])    # Output: True

print(elements["hydrogen"])
