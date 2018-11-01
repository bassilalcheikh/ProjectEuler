# Project Euler Problem 81: "Path Sum: Two Ways"
#
# Bassil Alcheikh
#
#
import numpy as np
from time import time

t_0 = time()

with open('matrix.txt') as file:
    filematrix = file.readlines()
    file.close()
   
# "string to integer matrix"
def stim(fileobject):
    numerical_matrix = []
    for i in fileobject:
        numerical_matrix.append([int(j) for j in i.split(',')])
    return numerical_matrix

npmatrix = np.array(stim(filematrix))

def triangularset(arr_object):
    indexsets = []
    sets = []
    for i in range(0, 2*(len(arr_object))-1):
        cache = []
        for j in range(0, i+1):
            cache.append((j, i-j))
        indexsets.append(cache[::-1])
    for a in indexsets:
        cache = []
        for b in a:
            try:
                cache.append(arr_object[b[0]][b[1]])
            except:
                pass
        sets.append(cache)
    return sets

# input: two vectors only
# output: one vector, triangle sums
def triangularsum(trisets):
    top = trisets[0]
    bottom = trisets[1]
    #print top, bottom
    if len(bottom) > len(top):
        updated_sums = [top[0]+bottom[0]]
        for i in range(1, len(top)):
            updated_sums.append(bottom[i]+min(top[i-1], top[i]))
        return updated_sums+[top[-1]+bottom[-1]]
    elif len(top) > len(bottom):
        updated_sums = []
        for i in range(0, len(bottom)):
            updated_sums.append(bottom[i]+min(top[i], top[i+1]))
        return updated_sums
    else:
        return "Error."

#input: triangle object
def findsumpaths(tri_object):
    for index in range(1, len(tri_object)):
        tri_object[index] = triangularsum(tri_object[index-1:index+1])
        print tri_object[index]
    #return len(tri_object)


print findsumpaths(triangularset(npmatrix))
#print time()-t_0

# times:
# (1) 0.081824 seconds