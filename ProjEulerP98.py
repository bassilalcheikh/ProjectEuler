# Project Euler Problem 98: "Anagramic Squares"
#
# Bassil Alcheikh
#
# conjecture: there are no "numerical anagrams" with 9 different digits (observation; not sure why)
# this conjecture rules out anagrams of size 9, as mappings wouldn't exist
#
from time import time

t_0 = time()

with open('words.txt', 'r') as file:
    lines = file.read()
    allwords = [word.strip('"') for word in lines.split(',')]
    file.close()

def findlongestword(li):
    maxlength = 0
    for word in li:
        if len(word) > maxlength:
            maxlength = len(word)
        else:
            continue
    return maxlength

def anagramsearch(li, str_len):
    domain = [l for l in li if len(l)==str_len]
    anagrams = []
    for i in range(0, len(domain)-1):
        for j in range(i+1, len(domain)):
            if i != j and sorted(domain[i]) == sorted(domain[j]):
                anagrams.append((domain[i], domain[j]))
    return anagrams

def ismapping(words, numbers):
    if type(words) != tuple or type(numbers) != tuple:
        pass
    elif len(words[0]) != len(numbers[0]):
        pass
    elif len(set(words[0])) != len(set(numbers[0])):
        pass
    else:
        set1 = sorted(zip(words[0], numbers[0]))
        set2 = sorted(zip(words[1], numbers[1]))
        return set1 == set2
        
allanagrams = []
for i in range(5, 15):
    allanagrams += anagramsearch(allwords, i)

numericalanagrams = []
for j in [5,6,7,8]:
    numericalanagrams += anagramsearch([str(i**2) for i in xrange(10**(j/2), 10**((j+1)/2))], j)

for word in allanagrams[::-1]:
    for num in numericalanagrams:
        if ismapping(word, num):
            print word, num
            break

print time()-t_0




# times:
# (1) 4.314261