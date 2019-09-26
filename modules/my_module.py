#####
# MY MODULE EXAMPLE
#####

print('Module imported')

string = 'Test'

def find_index(structure, target):
    for i, value in enumerate(structure):
        if value == target:
            return i
    
    return -1


# --------------------> <-------------------- #