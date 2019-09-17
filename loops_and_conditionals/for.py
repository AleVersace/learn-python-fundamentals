#####
# FOR
#####

nums = [1, 2, 3, 4, 5]

# For loop goes through a certain number of values
for num in nums:
    print(num)

print('\n')

# Break statement
for num in nums:            # Loops through the list
    if num == 4:            # Check if in any iteration num is equal to 4                
        print('Found 4!')   
        break               # If it is it prints 'Found 4!' and breaks (stops) the loop
    print(num)              # In fact print(5) is not included. 4 is not printed because print is after the if condition (and after the break)

print('\n')

for num in nums:            # Loops through the list
    if num == 4:            # Check if in any iteration num is equal to 4                
        print('Found 4!')   
        continue            # If it is it prints 'Found 4!' and skip the next instructions, continuing with the next iteration of the loop
    print(num)              # In fact print(5) is included. 4 is not printed again because print is after the if condition

print('\n')

# Loop within a Loop (nested loops)
for num in nums:                # For every num in nums print every letter in 'abc'
    for letter in 'abc':
        print(num, letter)

print('\n')

# Doing a certain number of iterations
for i in range(10):     # 0 to 9
    print(i)

print('\n')

for i in range(1, 11):  # 1 to 10
    print(i)

print('\n')

# String example
name = 'Ale347ssa384nd23ro'
for c in name:              # For every char c in the string
    if c.isalpha():         # If c is an alphabet char      (Filters the numbers)
        print(c)            # Print c


# --------------------> <-------------------- #