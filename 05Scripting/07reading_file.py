"""To read a file we have to create a file that we want to read
then we have to use a function called open(file_location, readmode)
After reading the content weha ve to make sure that we are closing the file reading activity using variable.close()"""

file_location = "/Users/mekalathuruchenchaiah/Desktop/PROGRAMMING/AI Programming with Python - Bertelsmann/05Scripting/my_file.txt"

f = open(file_location, "r")
file_data = f.read()
print(file_data)
print("content is being reading with open function :")
f.close()
print("*********")

# Some times we will forget the closing line which causes an issue at some point of time to read a file 
# Now we use another method which closes the file automatically when we use that to open a file -> with open(file_location, read_mode)

with open(file_location, "r") as f:
    file_content =f.read()
    print("content is being read by with open function :")
    print(file_content)