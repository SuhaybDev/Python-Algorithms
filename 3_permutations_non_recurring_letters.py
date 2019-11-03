# Import permutations from Python itertools module
from itertools import permutations

# Finding all possible permutations for the given string
perm = permutations('aab')

# Printing the permutations using a for loop
for i in list(perm):
    print(i)