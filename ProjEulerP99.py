# Project Euler Problem 99

# Find which line of the external file has the highest numerical value.

from math import log

results = []
with open('p099_base_exp.txt','r') as inputfile:
    for line in inputfile:
        results.append(line.strip().split(','))

def get_largest_pair(candidates):
    largest_pair = [1,1]
    for each_line in candidates:
        if float(each_line[1])*log(float(each_line[0])) > float(largest_pair[1])*log(float(largest_pair[0])):
            largest_pair = each_line
    return candidates.index(largest_pair)+1 # add 1 to adjust for "0-indexing"

print get_largest_pair(results)

# times:
# (1) 0.002197 seconds
