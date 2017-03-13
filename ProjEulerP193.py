# Project Euler Problem 193: Squarefree Numbers
#
# A positive integer n is called squarefree, if no square of a prime divides n,
# thus 1, 2, 3, 5, 6, 7, 10, 11 are squarefree, but not 4, 8, 9, 12. How many
# squarefree numbers are there below 2^50?
#
# http://www.challenge.nm.org/archive/09-10/ProjectEuler.net_193_Solution+Explanation.pdf
#
from alt_atkin import atkins13
from math import floor
from time import time

t_0 = time()

limit = 2**15

primes = atkins13(2**25+1)
sq_multiples = 0

for p in primes:
    sq_multiples += long(floor(limit/(p**2)))

print(long(limit**2-sq_multiples))

print(time()-t_0)
#print(2**50)
