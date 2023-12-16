VINIX = ['C', 'MA', 'BA', 'PG', 'CSCO', 'VZ', 'PFE', 'HD', 'INTC', 'T', 'V', 'UNH', 'WFC', 'CVX', 'BAC', 'JNJ', 'GOOGL', 'GOOG', 'BRK.B', 'XOM', 'JPM', 'FB', 'AMZN', 'MSFT', 'AAPL']
print(VINIX[1])
print(VINIX[-1])
print(len(VINIX))
print("BA" in VINIX)
print("VZ" not in VINIX)

# Lists are mutable 
# Strings in the lists are immutable
# Both Strings and lists are ordered which is why we are able to access the items using the indices 
 
VINIX[1] = "Chenchu"
print(VINIX)  # mutatioon happens the VINIX[1] will be replaced with "Chenchu"



greetings = "Hello there"
greeting = "Mello there"
print(greeting)                  # will be printed as Melli there
greetings[3] = "i" 
print(greetings)                 # TypeError: 'str' object does not support item assignment

