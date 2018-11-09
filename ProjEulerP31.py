# Project Euler Problem 31: "Coin Sums"
#
# Bassil Alcheikh, 2018
#
#
from time import time
from utilities import elemfrequency
t_0 = time()
limit = 200
denominations = [1, 2, 5, 10, 20, 50, 100, 200]
coin_vectors = [range(0, limit+1, i) for i in denominations]

def nextvector(v_1, v_2):
    sums = []
    for i_1 in v_1:
        for i_2 in v_2:
            x = i_1+i_2
            if x > limit:
                break
            else:
                sums.append(x)
    return sorted(sums)

def polymultiply(seed):
    while len(seed) > 1:
        cache = []
        for k in range(0, len(seed), 2):
            try:
                cache.append(nextvector(seed[k], seed[k+1]))
            except:
                cache.append(nextvector(seed[k], [0]))
        seed = cache
    return seed


print elemfrequency(polymultiply(coin_vectors)[0])[200]
print time()-t_0

# times:
# (1) 1.3151550293 seconds