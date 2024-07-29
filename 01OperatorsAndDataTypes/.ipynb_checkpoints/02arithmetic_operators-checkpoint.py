# The current volume of a water reservoir (in cubic metres)
# The amount of rainfall from a storm (in cubic metres)
# Use the multiplication assignment operator to decrease 
# the rainfall variable by 10% to account for runoff
reservoir_volume = 4.445e8
rainfall = 5e6
rainfall *= 0.9
print(rainfall)

# Use the addition assigment operator to add 
# the rainfall variable to the reservoir_volume variable
reservoir_volume += rainfall
print(reservoir_volume)

# Use the multiplication assignment operator to increase 
# reservoir_volume by 5% to account for stormwater that 
# flows into the reservoir in the days following the storm
reservoir_volume *= 1.05
print(reservoir_volume)

# Use the multiplication assignment operator to decrease 
# reservoir_volume by 5% to account for evaporation
reservoir_volume *= 0.95
print(reservoir_volume)

# Use the subtraction assignment operator to subtract 
# 2.5e5 cubic metres from reservoir_volume to account 
# for water that's piped to arid regions.
reservoir_volume -= 2.5e5
print(reservoir_volume)
