"""Sometimes we need more control over when a loop should end, or skip an iteration. In these cases, we use the break and continue keywords, 
which can be used in both for and while loops.
break terminates a loop
continue skips one iteration of a loop"""

manifest = [("bananas", 15), ("mattresses", 34), ("dog kernels", 42), ("machine", 120), ("cheeses", 5)]

weight = 0
items = []

for cargo in manifest:
    if weight >= 100:
        break
    else:
        items.append(cargo[1])
print(items)