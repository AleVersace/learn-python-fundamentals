#####
# STANDARD LIBRARY
#####

import sys
# print(sys.path)   # See the current sys path

# What will happen if we try to import a module from a different directory?
# Python can't find it
# We must add the path
sys.path.append('~/ale/Desktop/my_modules')
# print(sys.path)

# Or we can add to the PATH environment variable (Different from Linux to Windows)
# ---------- Linux ----------
# nano ~/.bash_profile
# export PYTHONPATH="~/ale/Desktop/my_modules"


# Standard Library is one of the best resources already written
# EXAMPLE

# Work with random module
import random

courses = ['Art', 'Maths', 'History', 'CS']
random_course = random.choice(courses)
print(random_course + '\n')


# Work with math module
import math

rads = math.radians(90)                     # pi/2
print('{}\n'.format(math.sin(rads)))        # 1


# Work with time and date module
import datetime
import calendar
today = datetime.date.today()
print(today)            # Today's date

print('{}\n'.format(calendar.isleap(2019))) # Leap year?


# Work with os module
import os

print(os.getcwd())      # Current working directory
print(os.__file__)      # Where the entire standard library is located


# --------------------> <-------------------- #