"""An if statement is a conditional statement that runs or skips code based on whether a condition is true or false. 
Here's a simple example."""

phone_balance = 3
bank_balance = 100
print(" Before recharge the phone balance is {} and the bank balance is {}".format(phone_balance, bank_balance))

if phone_balance < 5:
    phone_balance += 10
    bank_balance -= 10
    print("After recharge the phone balance is {} and the bank balance is {}".format(phone_balance, bank_balance))
