# Project Euler Problem 22
#
# What is the total of all the name scores in the file?
import names
names_AZ = names.names
names_AZ.sort() # this marks the step where all names are ordered alphabetically

letter_values = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9,
'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19,
'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26} # this can be more efficient (?) shorter, maybe

def name_value(name_str):
    sum_letter_values = 0
    for i in name_str:
        sum_letter_values += letter_values[i]
    return sum_letter_values

total_points = 0
for i,j in list(enumerate(names_AZ)):
    total_points += (i+1)*name_value(j)

print total_points

# times:
# (1) 0.2014461 seconds
# (2) 0.0082672 seconds (24.37 times faster! used "enumerate" instead of "index()" function)
