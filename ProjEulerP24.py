# Project Euler Problem 24: "Lexicographic Permutations"
#
# What is the millionth lexicographic permutation of the digits 0-9?
#
from math import factorial, floor

candidates = [i for i in range(0,10)]
perm_elem = []
index = 10**6-1

for j in range(9,-1,-1):
    n = index/factorial(j)
    perm_elem.append(str(candidates[n]))
    index = index - n*factorial(j)
    del candidates[n]

solution = ''.join(perm_elem)

# times:
# (1) 0.0 seconds
