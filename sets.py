#####
# SETS
#####

# Sets have no duplicate elements and unordered
# Elements of lists are inside { }

courses = {'History', 'Math', 'Physics', 'Art'}
print(courses)          # Try to execute and see the order of the print! (unordered)

courses.add('Computer Science')
courses.add('Art')      # This is a duplicate and will not be inserted
print(courses)

# Sets are useful to check efficiently if there is an element (Optimized for this)
print('Math' in courses)

# See values shered between sets (Optimized for this)
courses_1 = {'History', 'Math', 'Physics', 'Computer Science'}
courses_2 = {'History', 'Math', 'Design', 'Art'}

print(courses_1.intersection(courses_2))        # Returns a set with intersection between 2 sets.
print(courses_1.difference(courses_2))          # Difference
print(courses_1.union(courses_2))        # Union

# Emply Set (1 method)
empty_set = set()
# empty_set = {}        # Wrong! This will create an empty dictionary


# --------------------> <-------------------- #