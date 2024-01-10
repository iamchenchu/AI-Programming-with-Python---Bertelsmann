"""A function and a method look very similar. They both use the def keyword. They also have inputs and return outputs. The difference is 
that a method is inside of a class whereas a function is outside of a class."""


class Shirt:
    def __init__(self, shirt_color, size, shirt_style, shirt_price):
        self.color = shirt_color
        self.size = size
        self.style = shirt_style
        self.price = shirt_price
    def change_price(self, new_price):
        self.price = new_price
    def discount(self, discount):
        return self.price*(1-discount)
    
new_shirt = Shirt("Red", "L", "Sleeves", 20)

print(new_shirt.color)
print(new_shirt.size)
print(new_shirt.style)
print(new_shirt.price)

# Let's try to change the price
new_shirt.change_price(10)
print(new_shirt.price) # Price changed to 10 from 15
print(new_shirt.discount(0.2))

tshirt_collection = []

shirt_one = Shirt("Blue", "M", "Sleeves", 30)
shirt_two = Shirt("Red", "L","Without Sleeves",40 )
shirt_three = Shirt("Black", "XL", "Short Sleeves", 50)

tshirt_collection.append(shirt_one)
tshirt_collection.append(shirt_two)
tshirt_collection.append(shirt_three)
tshirt_collection.append(new_shirt)

for i in range(len(tshirt_collection)):
    print(tshirt_collection[i].color, tshirt_collection[i].size, tshirt_collection[i].style, tshirt_collection[i].price)




