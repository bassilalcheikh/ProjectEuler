# Project Euler Problem 59
#
# Bassil Alcheikh, 2018
#
from enchant import Dict

dictionary = Dict("en_US")

def elemfrequency(stuff):
    frequency = {}
    for element in stuff:
        # TODO what does the "set default" METHOD do?
        frequency.setdefault(element, 0)
        frequency[element] += 1
    return frequency

with open('cipher.txt') as file:
    data = file.read()
    data_string = str(data)
    components = data_string.split(',')
    #distribution = elemfrequency(components)
    # TODO PAY ATTENTION TO WHAT HAPPENS HERE
    #sorteddistro = sorted(distribution, key=distribution.get, reverse = True)

asciirange = range(32, 123)

def potentialnkey(keyindex):
    potential_key = []
    for nkey in asciirange:
        counter = 400
        i = 0
        while counter > 0: 
            if int(components[3*i+keyindex-1])^nkey in range(32,123):
                counter -= 1
                i += 1
            else:
                break
        if counter == 0: 
            potential_key.append(nkey)
    return potential_key

def threekeydecrypt(candidate_1, candidate_2, candidate_3, length):
    decrypted = []
    for x in range(0,length):
        decrypted.append(int(components[3*x+0])^candidate_1)
        decrypted.append(int(components[3*x+1])^candidate_2)                               
        decrypted.append(int(components[3*x+2])^candidate_3)
    return decrypted      

# checks if your code produced words or gibberish
def combotry(candidates_1, candidates_2, candidates_3):
    remove_ascii_set = range(33,65)+range(91,97) # this will be '(',')', '"', etc.
    for i in candidates_1:
        for j in candidates_2:
            for k in candidates_3:
                ascii_decrypted = threekeydecrypt(i, j, k, 64)
                words = []
                for t in ascii_decrypted:
                    if t not in remove_ascii_set:
                        words.append(t)
                test_string_v1 = ''.join([chr(w) for w in words])
                test_string_v2 = " ".join(test_string_v1.split())
                words = test_string_v2.split()
                word_counter = 0
                for s in words[:8]:  # "8" chosen arbitrarily; there are much more than 8 words 
                    if dictionary.check(s):
                        word_counter += 1
                        #print word_counter
                    else:
                        break
                if word_counter == 8:
                    return [i,j,k]

attempt = combotry(potentialnkey(1), potentialnkey(2), potentialnkey(3))

message_ascii = threekeydecrypt(attempt[0], attempt[1], attempt[2], int(len(components)/3))
print sum(message_ascii)+(int(components[-1])^attempt[0])
