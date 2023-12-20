"""In Python, you can create lists really quickly and concisely with list comprehensions. This example from earlier:"""
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
capitalized_cities = []
for city in cities:
    capitalized_cities.append(city.title())
print(capitalized_cities)

# We can reduce the above code to single line as below

capitalized_cities1 = [city.title() for coty in cities]
print(capitalized_cities1)
