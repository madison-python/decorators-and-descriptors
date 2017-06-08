# Steps:
#   1. Define a function.
#
#   2. Define a function that takes a single argument: another function. Have
#      it return another function that calls the function that was passed in.
#
#   3. "Wrap" the function from step 1 in a call to the function from step 2,
#       overwriting the original function.
#
#   4. Show the decorator syntax (just syntactic sugar!)


# Step 1

def floor_division(a, b):
    return a // b

# Step 2

# ...
