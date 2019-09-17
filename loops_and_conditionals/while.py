#####
# WHILE
#####

x = 0

# While loop goes until a certain condition is met
while x < 10:       # Goes until x is < 10
    print(x)
    x += 1          # We increment x

print('\n')

x = 1               # Starts from 1
while x < 10:
    print(x)        # 7 is printed because print is before the break statement
    if x == 7:
        break
    x += 2

print('\n')


# Infinite loop
x = 0
while True:         # The condition is always True, so the loop will never stop
    print(x)
    if x == 4:      # But this loop will end because of this condition istrution with the break statement
        break
    x += 1

print('\n')

# String example
name = 'Alessandro'
x = 0
c = name[0]
while c.isalpha():              # Not the fastest way to do this but useful to learn
    print(c.lower())
    x += 1
    if x < len(name):
        c = name[x]
    else:
        break



# --------------------> <-------------------- #