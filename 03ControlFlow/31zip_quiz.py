"""Use zip to write a for loop that creates a string specifying the label and coordinates of each point and appends it to the list points.
Each string should be formatted as label: x, y, z. For example, the string for the first coordinate should be F: 23, 677, 4."""

print("********QUESTION-1*************")
x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]
points = []
# write your for loop here
for point in zip(labels, x_coord, y_coord, z_coord):
    points.append("{}: {}, {}, {}".format(*point))

for point in points:
    print(point)

print("      ")
print("********QUESTION-2*************")
print("      ")
"""Use zip to create a dictionary cast that uses names as keys and heights as values."""

cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = {}

for name, height in zip(cast_names, cast_heights):
    cast = dict(zip(cast_names, cast_heights))
print(cast)


print("      ")
print("********QUESTION-3*************")
print("      ")

"""Unzip the cast tuple into two names and heights tuples."""
cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))
# define names and heights here
names, heights = (),() # replace with your code
names, heights = zip(*cast)
print(names)
print(heights)

print("      ")
print("********QUESTION-4*************")
print("      ")

"""Use zip to transpose data from a 4-by-3 matrix to a 3-by-4 matrix. There's actually a cool trick for this! Feel free to look 
at the solutions if you can't figure it out."""
data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))
data_transpose = tuple(zip(*data))
print(data_transpose)

print("      ")
print("********QUESTION-5*************")
print("      ")
"""Use enumerate to modify the cast list so that each element contains the name followed by the character's corresponding height. 
For example, the first element of cast should change from "Barney Stinson" to "Barney Stinson 72"."""

cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]

# Write your for loop here
for i, character in enumerate(cast):
    cast[i] = character + " " + str(heights[i])

print(cast)




