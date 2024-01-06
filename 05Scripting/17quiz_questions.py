"""Which module can tell you the current time and date?"""

import datetime
current_time = datetime.datetime.now()
print(current_time)

"""Which module has a method for changing the current working directory?"""
import os
# Change the current working directory to '/path/to/directory'
os.chdir('/Users/mekalathuruchenchaiah/Desktop/PROGRAMMING/AI Programming with Python - Bertelsmann/04Functions')
# You can then check the current working directory using os.getcwd()
current_directory = os.getcwd()
print(current_directory)

"""Which module can read data from a comma separated values (.csv) file into Python dictionaries for each row?"""
import csv
# Open the CSV file
with open('example.csv', mode='r') as file:
    # Create a DictReader object
    csv_reader = csv.DictReader(file)

    # Iterate over the rows in the CSV file
    for row in csv_reader:
        # Each row is a dictionary
        print(row)

"""Which module can help extract all of the files from a zip file?"""

import zipfile

# Path to the ZIP file
zip_path = 'path/to/your/zipfile.zip'
# Path where the extracted files will be stored
extract_to_path = 'path/to/extract/directory'
# Open the ZIP file in read mode
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    # Extract all the contents into the directory specified
    zip_ref.extractall(extract_to_path)


"""Which module can say how long your code took to run?"""



