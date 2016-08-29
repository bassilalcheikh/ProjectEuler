# Project Euler Problem 65: "Convergents of e"
#
# e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...]
#
# The first ten terms in the sequence of convergents for e are:
# 2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...
#
# The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.
#
# Find the sum of digits in the numerator of the 100th convergent of the
# continued fraction for e.
#
for i in range(1,34): e_dna += [1,2*i,1] # takes 0.00017 seconds

numerator = [2,3]

for i in range(2,100,1): numerator.append(e_dna[i]*numerator[i-1]+numerator[i-2])

sum_of_digits = sum([int(i) for i in list(str(numerator[-1]))])

# times:
# (1) 0.000136 seconds
