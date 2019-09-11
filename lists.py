#####
# LISTS
#####

# Lists are mutable collections, we can modify them.
# Elements of lists are inside [ ]

courses = ['History', 'Math', 'Physics', 'ComputerScience']
print(courses)
print(len(courses))
print(courses[0])           # Usage of index in lists
print(courses[3])

# Usage of negative index
print(courses[-1])          # Print the last one
print(courses[-2])

# print(courses[4])         # Index Error

print('\n')

# SLICING
print(courses[0:2])         # From 0 (included) to 2 (excluded)
print(courses[:2])
print(courses[1:])


print('\n')


# LIST METHODS
# Add Remove
courses.append('Art')       # Add a course to the list (at the end)
print(courses)

courses.insert(0, 'Algebra')    # Add 'Algebra' element in the position 0 of the list
print(courses)

courses_2 = ['Education', 'Machine Learning']
courses.extend(courses_2)                # We want to add multiple values (at the end)
print(courses)
# WARN: courses.insert(0, courses_2) will add the entire courses_2 list as a single element in the course list.

courses.remove('Art')
print(courses)

item = courses.pop()                    # Removes the last item (list usage as a stack or a queue), it returns the value
print(courses)
print(item)


print('\n')


# Order

courses.reverse()                       # Reverse order
print(courses)

courses.sort()                          # Sort items (str in alphabetical order)
print(courses)

nums = [1, 3, 7, 32, 2]
nums.sort()                             # Sort items (int in ascending order)
print(nums)                             

nums.sort(reverse=True)                 # Equals to nums.reverse()
print(nums)


print('\n')


# If we want to sort without altering the original list
nums = [1, 3, 7, 32, 2]
sorted_nums = sorted(nums)
print(sorted_nums)          # That is sorted
print(nums)                 # The original one wasn't touched


print('\n')


# Min, Max, Sum 
print(min(nums))
print(max(nums))
print(sum(nums))

print('\n')


# Find
courses = ['History', 'Math', 'Physics', 'ComputerScience']
print(courses.index('Math'))                # Print 'Math' index
print(courses.index('History'))
# print(courses.index('Art'))               # Error
print('Art' in courses)                     # Boolean result (Is there 'Art' in courses?)


print('\n')


# Loop
for item in courses:                        # Cicle the list calling every single cicle the element as 'item' and each time print it.
    print(item)

print('\n')

for index, course in enumerate(courses):    # Same cicle that prints also the index of the element
    print(index, course)

print('\n')

for index, course in enumerate(courses, start=1):    # Same cicle with numbers that starts from 1 instead of 0
    print(index, course)


print('\n')


# Join
courses = ['History', 'Math', 'Physics', 'ComputerScience']         
course_str = ', '.join(courses)                     # Join the elements of the list in a single string
print(course_str)                                   # This is a string

# Split
new_list = course_str.split(", ")                   # Splits the string taking ", " as sepator and returns a List of strings
print(new_list)                                     # This is a List of strings


print('\n')


# Empty List (2 methods)
empty_list = list()
empty_list = []


# --------------------> <-------------------- #