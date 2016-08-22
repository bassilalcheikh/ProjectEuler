# Project Euler Problem 92: "Square digit chains"

# Plan I:
# (1) for numbers 2 through 566, find all numbers with cycles resulting in 1
# (2) for all the numbers found in step (1), find their permutations, as long as
#     said permuations are less than 10,000,000
# (3) add numbers from step (2) to the list in step (1)
# (4) subtract the length of the master list in step (3) from 10,000,000
#
# Plan II:
# (1) for numbers 2 through 566, find all numbers with cycles resulting in 1
# (2) compare each number from 1 to 10**7 with the numbers resulting from (1),
#     looking at the int(list(sorted(n))) for each number n
# (3) if they match, increase "ones" counter by (you guessed it) 1
# (4) if they reach 89 first,

import time
t_0 = time.time()

ref_cache_ones = [1]
ref_cache_eightynines = [89]

# computes the sum of the digits' squares
def digits_squared_sum(number):
    return sum([int(i)**2 for i in str(number)])

# computes the sum of the digits' squares
def operation(number):
    cache = [number]
    while cache[-1] not in [1,89]:
        number = digits_squared_sum(number)
        cache.append(number)
    return cache

def store_numbers(list_of_numbers):
    if list_of_numbers[-1] == 1:
        for i in list_of_numbers[:-1]:
            ref_cache_ones.append(i)
            ref_cache_ones.append(int(str(i)[::-1])) #<-- is THIS necessary...?
    else:
        for j in list_of_numbers[:-1]:
            ref_cache_eightynines.append(j)
            #ref_cache_eightynines.append(int(str(j)[::-1]))  <-- is this necessary..?
    #return sorted(set(ref_cache_ones))
    return ref_cache_ones

for i in range(1,567):
    store_numbers(operation(i))

print sorted(set(ref_cache_ones)) # it takes ~0.021 seconds to get here
"""
ones = 0

for k in range(567,10**7):
    k = digits_squared_sum(k)

    if k in ref_cache_ones:
        ones += 1


print 10**7-1-ones
"""
t_1 = time.time()
print t_1-t_0

# times:
# (1) 166.8874 seconds
