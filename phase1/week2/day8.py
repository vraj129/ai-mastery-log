import math_utils

import math
from math import sqrt
import random
import datetime as dt

import os

print(math.sqrt(144))
print(math.pi)
print(math.floor(4.9))

print(random.randint(1, 100))
colours = ["red", "blue", "green", "yellow"]
print(random.choice(colours))

today = dt.date.today()
print(today)
print(type(today))

print(os.getcwd())

# --- 3 ways to import ---
print(sqrt(25))
print(dt.date.today())

print(math_utils.square(5))
print(math_utils.cube(3))
print(math_utils.is_even(8))
print(math_utils.is_even(7))