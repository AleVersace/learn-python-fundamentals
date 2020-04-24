### EXCEPTIONS

x = -1
# Handling
try:
    if x < 0:
        raise ValueError("Negative amount")     # Launch
except ValueError:
    print("Value Error")
except:
    print("An exception occurred")
else:
    print("Nothing went wrong")