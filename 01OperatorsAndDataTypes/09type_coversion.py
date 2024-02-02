print(type(4)) # Integer
print(type(3.7))
print(type('this'))
print(type(True))
print("0" + "5")
print(0 + 5)

mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"
#TODO: assign the total sales to a string with this format: This week's total sales: xxx
# You will probably need to write some lines of code before the assigning statement.
result_string = f"This week's total sales: {int(mon_sales)+int(tues_sales)+int(wed_sales)+int(thurs_sales)+int(fri_sales)}"
print(result_string)

weekly_sales = int(mon_sales) + int(tues_sales) + int(wed_sales) + int(thurs_sales) + int(fri_sales)
weekly_sales1 = str(weekly_sales)  #convert the type back!!
result_string1 = "This week's total sales: " + weekly_sales1
print(result_string1)




