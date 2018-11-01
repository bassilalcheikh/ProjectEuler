# Project Euler Problem 67: "Maximum Path Sum II"
#
# Bassil Alcheikh
#
#
import numpy as np
from time import time

t_0 = time()

with open('triangle.txt') as file:
    filematrix = file.readlines()
    file.close()
#print filematrix

# "string to integer matrix"
def stim(fileobject):
    numerical_matrix = []
    for i in fileobject:
        numerical_matrix.append([int(j) for j in i.split(' ')])
    return numerical_matrix

npmatrix = np.array(stim(filematrix))

# input: two vectors only
# output: one vector, triangle sums
def maxtriangularsum(trisets):
    top = trisets[0]
    bottom = trisets[1]
    #print top, bottom
    if len(bottom) > len(top):
        updated_sums = [top[0]+bottom[0]]
        for i in range(1, len(top)):
            updated_sums.append(bottom[i]+max(top[i-1], top[i]))
        return updated_sums+[top[-1]+bottom[-1]]
    elif len(top) > len(bottom):
        updated_sums = []
        for i in range(0, len(bottom)):
            updated_sums.append(bottom[i]+max(top[i], top[i+1]))
        return updated_sums
    else:
        return "Error."

#input: triangle object
def findsumpaths(tri_object):
    for index in range(1, len(tri_object)):
        tri_object[index] = maxtriangularsum(tri_object[index-1:index+1])
        print max(tri_object[index])
    return len(tri_object)


print findsumpaths(npmatrix)
print time()-t_0

# times:
# (1) 0.005229950 seconds