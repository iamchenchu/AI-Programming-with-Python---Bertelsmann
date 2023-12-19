# Fill in the conditionals below to inform the user about how
# their guess compares to the answer.

answer = 50 #replace 0 with a value you choose
guess = 30 #replace 0 with a value you choose

if guess <= answer : #provide conditional
    result = "Oops!  Your guess was too low."
    print(result)
elif guess >= answer: #provide conditional
    result = "Oops!  Your guess was too high."
    print(result)
else:
    result = "Nice!  Your guess matched the answer!"
    print(result)