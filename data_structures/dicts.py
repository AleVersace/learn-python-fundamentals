#####
# DICTIONARIES
#####

# Dicts are in other languages called HashMaps or Associative Arrays
# Every element has a 'key' and a 'value' that are strictly correlated
# The key is unique
# Elements of lists are inside { }

# 'key': 'value'    In this case all keys are strings
student = {'name': 'Alessandro', 'age': 21, 'courses': ['Math', 'Algorithms']}
print(student)
print(student['name'])          # How to access with key
print(student['courses'])
# print(student['phone'])       # KeyError!


print('\n')

# Access
print(student.get('name'))
print(student.get('phone'))                 # Returns None
print(student.get('phone', 'Not found'))    # Returns Not found


print('\n')


# Update
student['phone'] = '123456'                 # If already exists will override the value
print(student.get('phone'))
student.update({'name': 'Lara', 'age': 26}) # Update values
print(student)


print('\n')


# Delete
del student['phone']
print(student)
age = student.pop('age')            # Removes and return the value
print(age)


print('\n')


# Other useful methods
print(len(student))         # Number of keys
print(student.keys())       # All Keys
print(student.values())     # All Values
print(student.items())      # All 'Pairs'


print('\n')


student = {'name': 'Alessandro', 'age': 21, 'courses': ['Math', 'Algorithms']}
for key in student:         # Loops through the keys
    print(key)

print('\n')

for key, value in student.items():
    print(key, value)       # Loops through keys and values


# --------------------> <-------------------- #