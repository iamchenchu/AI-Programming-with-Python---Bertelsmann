x = int(4.7)   # x is now an integer 4
y = float(4)   # y is now a float of 4.0
print(type(x))
print(type(y))
print(.1 + .1 + .1)
print(.1 + .1 + .1 == .3) # False

import math
print(math.isclose(0.1 + 0.1 + 0.1, 0.3))