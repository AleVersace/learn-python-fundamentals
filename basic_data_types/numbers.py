#####
# NUMBERS
#####


num_1 = 3
num_2 = 3.14


print(num_1)
print(type(num_1))       # Type Int
print(type(num_2))       # Type Float


# ARITHMETIC

# Arithmetic Operators:
# Addition:         3 + 2
# Subtraction:      3 - 2
# Multiplication:   3 * 2
# Division:         3 / 2
# Floor Division:   3 // 2      # Removes the decimal part
# Exponent:         3 ** 4
# Modulus:          3 % 2

# Try
print('Prova operazioni base:')
print(7 % 4)

# Arithmetic variables
num = 3
num = num + 4
print('Prova somma num = num + 1:')
print(num)      # 7

num = 2
num *= 4
print(num)      # 8

print('\n')

# Absolute value
num = -10
num = abs(num)
print(num)  # 10

# Rounding
print(round(3.75))
print(round(3.45))
print(round(3.75, 1))
print(round(3.762, 2))

print('\n')

# COMPARISONS:
# Equal:            3 == 2
# Not Equal:         3 != 2
# Greater Than:     3 > 2
# Less Than:        3 < 2
# Grater or Equal:  3 >= 2
# Less or Equal:    3 <= 2

num_1 = 3
num_2 = 2

print('Comparisons:')
print(num_1 == num_2)   # Returns and prints a boolean
print(num_1 != num_2)
print(num_1 <= num_2)

print('\n')


#####
# STRINGS AND NUMBERS (CASTING)
#####

num_1 = '100'   # Those are strings!
num_2 = '200'

# We want to add these two numbers, but those are strings!
print(num_1 + num_2)    # This will chain the two strings

num_1 = int(num_1)      # This is a 'cast'
num_2 = int(num_2)      # Now these are integers!

print(num_1 + num_2)


# --------------------> <-------------------- #