# Pandigital Products
#
# The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing
# multiplicand, multiplier, and product is 1 through 9 pandigital.
#
# Find the sum of all products whose multiplicand/multiplier/product identity
# can be written as a 1 through 9 pandigital.
# -----------------------------------------------------------------------------
# Two general cases:
#   (1) 1 digit x 4 digits = 4 digits
#   (2) 2 digits x 3 digits = 4 digits
# -----------------------------------------------------------------------------
#
from time import time
t_0 = time()
stuff = []

#case 1:
for i in range(1234,9876):
    if len(stuff)==9:
        break
    else:
        for j in range(1,9+1):
            entry = str(i)+str(j)+str(i*j)
            if len(set(entry))==len(entry) and len(entry)==9 and all(c not in '0' for c in entry):
                stuff.append(i*j)

#case 2:
for i in range(123,987):
    if len(stuff)==108:
        break
    for j in range(12,99):
        entry = str(i)+str(j)+str(i*j)
        if len(set(entry))==len(entry) and len(entry)==9 and all(c not in '0' for c in entry):
            stuff.append(i*j)

print(sum(set(stuff)))
print(time()-t_0)

# times:
# (1) 0.31100011 seconds
# (2) 0.30599999 seconds

