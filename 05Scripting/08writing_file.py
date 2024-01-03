# Writing to the file 
"""Read Mode ('r'): This mode is used to read data from an existing file. If the file does not exist, it raises an IOError.
Write Mode ('w'): This mode is used for writing data to a file. If the file exists, it will be overwritten. If the file does not exist, it will be created.
Append Mode ('a'):This mode is used to append data to an existing file. If the file does not exist, it creates a new file for writing.
Read and Write Mode ('r+'): This mode is used to read and write data into the same file. The file must exist; otherwise, it raises an IOError.
Write and Read Mode ('w+'): Similar to 'r+', but if the file does not exist, it will create a new one. If the file exists, it will be overwritten.
Append and Read Mode ('a+'): This mode allows you to read and append data to a file. If the file does not exist, it creates a new one.
Binary Modes: By adding 'b' to the modes above (like 'rb', 'wb', 'ab', 'r+b', 'w+b', 'a+b'), you can work with files in binary format. This is particularly useful for non-text files like images or executable files."""

path = "/Users/mekalathuruchenchaiah/Desktop/PROGRAMMING/AI Programming with Python - Bertelsmann/05Scripting/my_file.txt"
f = open(path, 'r+')
f.write("\nI am writing this line to the file to test the functionality of the write() function in python")
content = f.read()
print(content)
f.close()