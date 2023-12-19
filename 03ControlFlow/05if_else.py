points = 174  # use this input to make your submission

# write your if statement here
if points < 50 & points > 1 :
    result = "Congratulations! You won a wooden rabbit!"
    print(result)
elif points < 150 & points > 50 :
    result = "Congratulations! You won a no prize!"
    print(result)
elif points < 180 & points > 150 :
    result = "Congratulations! You won a wafer-thin mint!"
    print(result)
elif points < 200 & points > 181 :
    result = "Congratulations! You won a penguin!"
    print(result)
else:
    result = "Oh dear, no prize this time."
    print(result)