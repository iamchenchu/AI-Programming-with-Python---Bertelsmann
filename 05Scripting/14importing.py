"""We can actually import Python code from other scripts, which is helpful if you are working on a bigger project where you want to organize
your code into multiple files and reuse code in those files. If the Python script you want to import is in the same directory as your 
current script, you just type import followed by the name of the file, without the .py extension.
import useful_functions"""

import useful_functions as uf

scores = [88, 92, 79, 93, 85]

mean = uf.mean(scores)
curved = uf.add_five(scores)

mean_c = uf.mean(curved)

print("Scores:", scores)
print("Original Mean:", mean, " New Mean:", mean_c)

print(__name__)

#print(uf.__name__)

