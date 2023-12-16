VINIX = ['C', 'MA', 'BA', 'PG', 'CSCO', 'VZ', 'PFE', 'HD', 'INTC', 'T', 'V', 'UNH', 'WFC', 'CVX', 'BAC', 'JNJ', 'GOOGL', 'GOOG', 'BRK.B', 'XOM', 'JPM', 'FB', 'AMZN', 'MSFT', 'AAPL']
print(VINIX[1])
print(VINIX[-1])
print(len(VINIX))
print("BA" in VINIX)
print("VZ" not in VINIX)

#Lists are mutable 
# Strings in the lists are immutable 
VINIX[1] = "Chenchu"
print(VINIX) 

greetings = "Hello there"
greetings[3] = "i" 
print(greetings) # TypeError: 'str' object does not support item assignment

