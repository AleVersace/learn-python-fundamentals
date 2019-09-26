#####
# MODULES USAGE EXAMPLE
#####

courses = ['Art', 'Maths', 'History', 'CS']

# Import the module and use an alias
import my_module as m

# Use the module
index = m.find_index(courses, 'History')
print(index)

# Import a single function and a single variable
from my_module import find_index, string
print(string)

# Import all
from my_module import *



# --------------------> <-------------------- #