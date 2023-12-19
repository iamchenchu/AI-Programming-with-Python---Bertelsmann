#Creating a modyfying lists
cities = ["new york", "mounten view", "chicago", "loss angels"]
capitalized_cities = []

for index in range(len(cities)):
    capitalized_cities.append(cities[index].title())
    print(cities[index].title())
print(capitalized_cities)