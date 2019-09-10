# BASIC STRINGS

# This is a comment

# This is a variable (usually name is lower case, multiple words separated by '_')
message = "Hello World!"
my_message = "A new Hello World"

# Output function
print("Hello World")
print(message)
print(my_message)

# We could use '' or "" for strings.. "" are useful when we need ' inside a phrase
phrase = "Alessandro's World"
print(phrase)

# Or we can "skip" a character with a \
phrase = 'Alessandro\'s World'
print(phrase)

# Use a String as an array of characters
message = 'Hello World'
print(message[0])           # First character (position 0)
print(message[10])          # Last character (The string length is 11, but we start couting positions from 0)


print('\n')


#SOME SLICING
print(message[0:4])         # From the first index (included) to the second index (excluded)
print(message[0:5])

print(message[:5])          # From the beginning to 5 (always excluded)
print(message[6:])          # From 6 included to the end


print('\n')


# SOME STRING METHODS
message = 'Hello World'
print(message + ' ' + message)  # Strings chaining with +.. Be careful on spaces!
print(len(message))             # Length of a string

print(message.lower())          # All lower case
print(message.upper())          # All upper case

print(message.count('l'))       # Count the number of occurrencies of the 'l' in the string
print(message.find('World'))    # Finds the index of the beginning of the occurence.
print(message.find('Moon'))     # Prints a -1 that means no occurrence, so no index

print('\n')

message = 'Hello World'
message.replace('World', 'Universe')    # Replace 'World' with 'Universe' and returns the new string
print(message)                          # But replace doesn't modify the original variable

new_message = message.replace('World', 'Universe')
print(new_message)

# If we want to change the original string we can do this.
message = message.replace('World', 'Moon')
print(message)


print('\n')


# STRING CHAINING

first = 'Alessandro'
last = 'Versace'

message = first + ' ' + last + ', welcome!'
print(message)

message2 = '{} {}, welcome!'.format(first, last)    # Easier version for complex chaining
print(message2)

# ONLY 3.6+ version
message3 = f'{first} {last}, welcome! (with f)'
print(message3)

print('\n')

# print(dir(first))       # See all avaiable methods for this type of data
# print(help(str))        # See all avaiable methods with explaination

print(help(str.lower))      # See documentation about a specific method


# --------------------> <-------------------- #