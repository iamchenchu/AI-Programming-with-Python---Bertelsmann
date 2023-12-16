sentence1 = "I wish to register a complaint."
sentence2 = ["I", "wish", "to", "register", "a", "complaint", "."]

sentence2[6]="!"
print(sentence2)
sentence2[0]= "Our Majesty"
print(sentence2)
sentence2[0:2] = ["We", "want"]
print(sentence2)

sentence1[30]="!"
print(sentence1)

#For sentence 2 it will be mutated and the execution will be done as expected 
#for sentemce 1 we are taking only one string, but not as a list so it can not be mutated 




