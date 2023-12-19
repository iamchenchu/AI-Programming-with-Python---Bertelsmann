"""Write a for loop that iterates over a list of strings, tokens, and counts how many of them are XML tags. XML is a data language similar 
to HTML. You can tell if a string is an XML tag if it begins with a left angle bracket "<" and ends with a right angle bracket ">". 
Keep track of the number of tags using the variable count.

You can assume that the list of strings will not contain empty strings."""

#Code 

tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

# write your for loop here
for number in range(len(tokens)):
    if (tokens[number][0] == "<") and (tokens[number][-1]):
        count +=1
print(count)