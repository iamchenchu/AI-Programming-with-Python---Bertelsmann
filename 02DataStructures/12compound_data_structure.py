"""Try your hand at working with nested dictionaries. Add another entry, 'is_noble_gas,' to each dictionary in the `elements`
 dictionary. After inserting the new entries you should be able to perform these lookups:
```python
>>> print(elements['hydrogen']['is_noble_gas'])
False
>>> print(elements['helium']['is_noble_gas'])
True
```
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
