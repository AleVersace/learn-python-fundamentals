#####
# TUPLES
#####

# Tuples are immutable, so we can't modify them.
# Elements of lists are inside ( )


# Example with list on why we need Tuples:

list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1                 # We are inizializing list_2 pointer to list_1

print(list_1)
print(list_2)

# So if we change list_1 we are also changing list_2
list_1[0] = 'Art'

print(list_1)
print(list_2)


print('\n')


# Immutable Tuples:
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# tuple_1[0] = 'Art'        # This will give an error!

# print(tuple_1)
# print(tuple_2)


print('\n')


# Empty Tuple (2 methods)
empty_tuple = tuple()
empty_tuple = ()


# --------------------> <-------------------- #