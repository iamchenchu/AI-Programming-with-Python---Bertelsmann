"""Write a function named `population_density` that takes two arguments, `population` and `land_area`, and returns a population density calculated from those values."""
# write your function here
def population_density(population, land_area):
    density = population/land_area
    return density
print(population_density(1000, 20))

"""Write a function named readable_timedelta. The function should take one argument, an integer days, and return a string that says how many weeks and days that is. For example,
calling the function and printing the result like this:

print(readable_timedelta(10))
should output the following:
1 week(s) and 3 day(s)."""

# write your function here
def readable_timedelta(days):
    weeks = days // 7
    days = days % 7
    return "{} week(s) and {} day(s).".format(weeks, days)


print(readable_timedelta(1))
    