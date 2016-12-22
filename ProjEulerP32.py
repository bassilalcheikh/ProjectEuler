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
def pandigital_quality(x,y,z):
    if len(set(str(x)+str(y)+str(z)))==len(str(x))+len(str(y))+len(str(z)):
        #print(set(str(x)+str(y)+str(z)))
        return True

products = []
for i in range(1234,9876+1):
    for j in range(1,9):
        if pandigital_quality(j,i,int(float(i)/j)) and i%j==0:
            products.append(i)
            #print(str(j)+"x"+str(int(float(i)/j))+"="+str(i))

first_cut = set([k for k in products if all(c not in '0' for c in str(k))])

print first_cut

for a in range(1234,9876+1):
    for b in range(12,617):
        if pandigital_quality(a,b,int(float(a)/b)) and a%b==0:
            products.append(a)

second_cut = set([k for k in products if all(c not in '0' for c in str(k))])
print(time()-t_0)

print(sum(second_cut))
