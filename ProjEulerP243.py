# Project Euler Problem 243: "Resilience"
#
# Bassil Alcheikh
#
#
from time import time
from decimal import Decimal
from eratosieve import eratolist as el
from operator import mul

t_0 = time()

threshold = Decimal(15499)/94744
primes = el(50000)

def phiprimebases(primes, limit):
    n = 1
    i = 0
    phi = 1
    while phi >= (n-1)*limit:
        n = reduce(mul, primes[0:i+1], 1)
        phi *= int(primes[i]*(1-Decimal(1)/primes[i]))
        i += 1
    return n/primes[i-1], primes[0:i-1], phi/(primes[i-1]-1)

def primefinetuning(base_product, list_of_primes, base_number_totient):
    results = []
    nextprime = primes[primes.index(list_of_primes[-1])+1]
    for x in range(1, nextprime):
        if x in list_of_primes:
            pass
        else:
            number = base_product * x
            number_totient = base_number_totient * x
            if float(number_totient)/(number - 1) < threshold:
                #print x, float(number_totient)/(number - 1), threshold
                results.append(x)
            #results.append(int(number_totient < (number-1)*threshold)*x)
    return min(results)

primes_needed = phiprimebases(primes, threshold)

fine_tuned_multiple = primefinetuning(primes_needed[0], primes_needed[1], primes_needed[2])

print primes_needed[0]*fine_tuned_multiple

print time()-t_0

# times:
# (1) 0.00926113 seconds