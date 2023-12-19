# number to find the factorial of
number = 6   
# start with our product equal to one
product = 1
# track the current number being multiplied
current = 1
# write your while loop here
while current <= number :
    product *=number
    number -= 1

print("The Factorial of {} is : {}".format(number, product))
    
# Below is the code using the for loop

# number to find the factorial of
number = 6   
# start with our product equal to one
product = 1
# write your for loop here
for i in range(6):
    product = product*number
    number = number -1
print(product)