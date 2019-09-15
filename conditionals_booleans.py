#####
# CONDITIONALS AND BOOLEANS
#####

# Booleans can take 2 values: True of False
# Conditional costructs execute code depending on some conditions (booleans)

# Example
if True:
    print('This is True')       # Indentation is important!

if False:
    print('This is True')

print('\n')

# COMPARISONS:
# Object Identity:      is          # Same object in memory
# Equal:                ==          # Equals content, not the same in memory
# Not Equal             !=
# Greater Than:         >
# Less Than:            <
# Grater or Equal:      >=
# Less or Equal:        <=


# IF ELSE

language = 'Italian'                # Booleans are variables
language = 'French'

if language == 'Italian':           # == usage for comparison
    print('This is Italian!')
else:                               # if language is not == 'Italian'
    print('This is not Italian!')

print('\n')

# IF ELSE ELIF

if language == 'Italian':
    print('This is Italian!')
elif language == 'French':
    print('This is French!')
elif language == 'Spanish':
    print('This is Spanish')
else:
    print('This is not Italian!')


print('\n')


# AND OR NOT

user = 'Alessandro'
logged = True

if user == 'Alessandro' and logged == True:         # Execute code only if user is Alessandro and it is logged
    print('Execute!')
else:
    print('Not logged in or not Alessandro')

print('\n')

user = 'Clara'
logged = True

if user == 'Alessandro' or logged == True:         # Execute code only if user is Alessandro or it is logged
    print('Execute!')
else:
    print('Not logged in and not Alessandro')

print('\n')

if user == 'Alessandro' or logged == True:         # Execute code only if user is Alessandro or it is logged
    print('Execute!')
else:
    print('Not logged in and not Alessandro')

print('\n')

logged = False

if not logged:                  # Equals to if logged == False
    print('You are not logged!')
else:
    print('Execute!')


print('\n')


a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)   # Are these equals? (content) YES
print(a is b)   # Are these really the same object in memory? NO
print(id(a))    # Ids are not the same
print(id(b))

print('\n')

b = a           # b will point to the same item of a
print(a is b)   # Ids are the same
print(id(a))
print(id(b))


print('\n')


# FALSE VALUES
# False
# None
# Zero (Any numeric type)
# Empty sequence IE. '', (), []
# Empty map/dict {}

condition = {}    # Try all the above!

if condition:
    print('This is True')
else:
    print('This is False')


# --------------------> <-------------------- #