try:
    x = int(input("Please enter the number : "))
    y = int(input("Please enter the number : "))
    z = x/y
except ZeroDivisionError as e:
   # some code

   print("ZeroDivisionError occurred: {}".format(e))
