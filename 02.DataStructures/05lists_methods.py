months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
print(len(months)) # Prints the length of list
print(max(months)) # Prints the max element in the list
print(min(months)) # Prints the min of the list
print(sorted(months)) # Prints the sorted list
months.append("Year") # Adds Year to the the end of the list
print(months)

#Note : we can use the join only incase of the strings 
print("\n".join(months)) # Prints one by one each in new line
print("->".join(months)) # Adds the "->" string to each value in a single line 



days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
print(sorted(days_in_month, reverse=True)) # Revers order will be printed 

name = "Jim"
student = name
name = "Tim"
print(name) # Tim which is most recent saved in the name variable
print(student) # Jim  which is most recent saved in the name variable


scores = ["B", "C", "A", "D", "B", "A"]
grades = scores
print("Scores are :",scores) 
print("Grades are :", grades)