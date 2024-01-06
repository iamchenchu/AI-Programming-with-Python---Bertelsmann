"""Create a function that opens the flowers.txt, reads every line in it, and saves it as a dictionary. The main (separate) function should 
take user input (user's first name and last name) and parse the user input to identify the first letter of the first name. It should then
use it to print the flower name with the same first letter (from dictionary created in the first function)."""

path = "05Scripting/flowers.txt"
## function that creates a flower_dictionary from filename
def create_flowerdict(filename):
    flower_dict = {}
    with open(filename) as f:
        for line in f:
            letter = line.split(": ")[0].lower() 
            flower = line.split(": ")[1].strip()
            flower_dict[letter] = flower
    return flower_dict

## Main function that prompts for user input, parses out the first letter
## includes function call for create_flowerdict to create dictionary
def main(): 
    flower_d = create_flowerdict(path)
    full_name = input("Enter your First [space] Last name only: ")
    first_name = full_name[0].lower()
    first_letter = first_name[0]
## print command that prints final input with value from corresponding key in dictionary
    print("Unique flower name with the first letter: {}".format(flower_d[first_letter]))

main()

