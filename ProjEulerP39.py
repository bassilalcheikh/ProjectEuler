# Project Euler Problem 39: "Integer right triangles"
#
# Bassil Alcheikh
#
from utilities import elemfrequency
from time import time

t_0 = time()

def pythagoreantriple(m,n):
    if m < n:
        return None
    else:
        a = m**2 - n**2
        b = 2*m*n
        c = m**2 + n**2
        return (a,b,c)

def pythagomultiple(pyth, limit):
    multiples = []
    end_limit = limit/max(pyth)+1
    for k in xrange(1, end_limit+1):
        multiples.append((k*pyth[0], k*pyth[1], k*pyth[2]))
        #k += 1
    return multiples

# upper limits of 23 and 24 should work because 23**2, 24**2 are minimum squares above 500,
# implying that the right side of the equation is also 500, implying no sum less than 500, so we 
# don't miss out on any (primitive?) pythagorean triples

pythtriples = []
for i in range(1,24):
    for j in range(i+1, 25):
        if i == j:
            continue
        else:
            pythtriples += pythagomultiple(pythagoreantriple(j,i), 1000)

sorted_triples =  [tuple(sorted(trip)) for trip in pythtriples]
unique_sorted_triples = list(set(sorted_triples))

sums = [sum(t) for t in unique_sorted_triples if sum(t) < 1001]

print max(elemfrequency(sums), key=elemfrequency(sums).get)

print time()-t_0

# times:
# (1) 0.003583908 
# (2)
