# Project Euler Problem 62: "Cubic Permutations"
# Difficulty Level: 15%
#
# Find the smallest cube for which exactly five permutations of its digits are cube.

import collections

cubes_str_bits = [list(str(x**3)) for x in range(1000,8385,1)]

X = [sorted(i) for i in cubes_str_bits]
Y = [''.join(k) for k in X]

for key, value in dict(collections.Counter(Y)).items():
    if value == 5:
        print (1000+Y.index(key))**3

# times:
# (1) 0.035427 seconds
