# Project Euler Problem 27: "Quadratic Primes"
#
# Bassil Alcheikh
#
from eratosieve import eratogen

def isprime(p):
    if p == 0 or p== 1:
        return False
    if p < 0:
        p = -p
    for i in xrange(2, int(p**0.5)+1):
        if p%i == 0:
            return False
    return True    

biggest_point = (0,0,0)

for b in eratogen(1000):
    for a in xrange(-999,1000,2):
        f = lambda n: n**2 + a*n + b
        sentinel = True
        x = 0
        while sentinel:
            if isprime(f(x)):
                x += 1
            else:
                sentinel = False
        if x > biggest_point[2]:
            biggest_point = (a,b,x)

print biggest_point[0]*biggest_point[1]

# times
# (1) 1.67107 seconds
# (2) 1.47338 seconds
# (3) 0.74567 seconds (time halved by using generators instead of lists)
