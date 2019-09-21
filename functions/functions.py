#####
# FUNCTIONS
#####

# Functions are parts of code that can be called and executed in our program
# Functions are useful to add modularity and readability to our code


def hello_world():  # Definition of a function with a name (in this case 'hello_world')
    pass  # Pass means that we are leaving the function empty


hello_world()  # Call of the function -> Here the code in the function will be executed (but now it's empty)
print(hello_world())  # This will print none

print("\n")

# Let's create another (more useful) funtion
def welcome():
    print('Welcome! This is my program!')

welcome()       # This will recall our function and execute the code inside of it

print('\n')

# USAGE: If we have to use a portion of code different times in a program, we can create a function and call it every time we want.
# USAGE: Also if we need to change the code, we don't have make changes in different parts of the program, but we just have to change the code in the function
# Common practice is to add comments before to say what the function is going to do

# PARAMETERS

def welcome_home(name):                     # Name is a parameter, that the function will use for its purpouse
    print('Hey %s! Welcome home!' % name)   # %s will concatenate the 2 strings

name = 'Alessandro'
welcome_home(name)              # We are calling our function passing name as parameter


# !WARN: Parameters that we pass can have different name from parameters that the function is going to receive
surname = 'Cooper'
welcome_home(surname)

print('\n')


# RETURNS

# This function will calculate the cost of multiple objects purchase
def total_cost(unitarian_cost, number):
    return unitarian_cost*number        # We are doing a multiplication and returning the result

number_of_pencils = 11
cost_per_pencil = 1.60

total_price = total_cost(cost_per_pencil, number_of_pencils)    # Calling the function, passing our parameters and save the result in the variable total_price
print(total_price)
print(total_cost(cost_per_pencil, number_of_pencils))           # Same thing

print('\n')


# We can see functions as black boxes and just know what we have to pass and what it will return
# for example
def welcomeTo(name):
    return 'Welcome home %s' % name     # Return 2 strings chained in a single string

name = 'Alessandro'
print(welcomeTo(name).upper())   # We are calling the function that returns a string, then it calls upper() oh the returned string 

print('\n')

# Example with conventions *args and **kwargs. 

def student_info(*args, **kwargs):
    print('args: {}'.format(args))      # Chained elements
    print('kwargs: {}'.format(kwargs))  # Chained elements

# *args is a touple and **kwargs result in a dictionary/map
student_info('Art', 'Maths', 'History', name = 'Alessandro', age = 21)

print('\n')

# Here kwargs will result empty, because we haven't inserted any key = value
student_info(21, 23, 45, 'Name', 'Surname')

print('\n')

# If we want to pass a list and a dict we have to 'Unpack' them with * and ** while passing them
courses = ['Art', 'Maths', 'History']
student = {'name': 'Alessandro', 'age': 21}

# student_info(courses, student) # Try this, doesn't work!
student_info(*courses, **student)

print('\n')


###### TRY USING THEM!


# --------------------> <-------------------- #
