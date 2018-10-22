# Project Euler Problem 89: "Roman Numerals"
#
# Bassil Alcheikh
#
#from time import time

#t_0 = time()
numeralsdictionary = {'M':1000, 'D': 500, 'C': 100, 'L': 50, 'X':10, 'V':5, 'I':1}
numeralsvector = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
subtractive_pairs = {'I':('V','X'), 'X':('L','C'), 'C':('D','M')}

test_answers = {
    '804': 'DCCCIV', 
    '904': 'CMIV',
    '94': 'XCIV',
    '84': 'LXXXIV',
    '19': 'XIX',
    '14': 'XIV',
    '999': 'CMXCIX',
    '444': 'CDXLIV',
    '49': 'XLIX',
    '44': 'XLIV',
    '809': 'DCCCIX',
    '409': 'CDIX',
    '4': 'IV',
    '9': 'IX',
    '45': 'XLV',
    '39': 'XXXIX',
    '92': 'XCII',
    '99': 'XCIX',
    '59': 'LIX'
}
test_cases = [
    804,  
    904, 
    94, 
    84, 
    19, 
    14, 
    999, 
    444, 
    49, 
    44, 
    809, 
    409, 
    4, 
    9, 
    45, 
    39, 
    92, 
    99, 
    59
]

# "validromans" takes a number and produces the minimal Roman Numeral version of said number
def validromans(n):
    roman_string = ''
    thousands = n/1000
    n -= thousands*1000
    five_hundreds = n/500
    n -= five_hundreds*500
    one_hundreds = n/100
    n -= one_hundreds*100 
    fifties = n/50
    n -= fifties*50
    tens = n/10
    n -= tens*10
    fives = n/5
    n -= fives*5
    ones = n/1
    n -= ones*1
    breakdown = [thousands, five_hundreds, one_hundreds, fifties, tens, fives, ones]
    for i,j in enumerate(breakdown):
        roman_string += j*str(numeralsvector[i])
    return roman_string

def efficient(r_n):
    if len(r_n) > 1:
        numerallist = list(r_n)
        if len(set(r_n[0:4])) == 1 and (r_n[0] != 'M'):
            numerallist[1] = subtractive_pairs[r_n[0]][0]
            numerallist[2] = ''
            numerallist[3] = ''
        for i in range(0, len(r_n)-4):
            if len(set(r_n[i+1:i+5])) == 1:
                if r_n[i]==subtractive_pairs[r_n[i+1]][0]:
                    numerallist[i] = r_n[i+1]
                    numerallist[i+1] = subtractive_pairs[r_n[i+1]][1]
                    for j in range(2,5):
                        numerallist[i+j] = ''
                else:
                    numerallist[i+1] = r_n[i+2]
                    numerallist[i+2] = subtractive_pairs[r_n[i+1]][0]
                    for j in range(3,5):
                        numerallist[i+j] = ''
        return ''.join(numerallist)
    else:
        return r_n

def readromans(romanstring):
    romanreverse = romanstring[::-1]
    regnumber = numeralsdictionary[romanreverse[0]]
    for i in range(1,len(romanreverse)):
        if numeralsdictionary[romanreverse[i]] < numeralsdictionary[romanreverse[i-1]]:
            regnumber -= numeralsdictionary[romanreverse[i]]
        else:
            regnumber += numeralsdictionary[romanreverse[i]]
    return regnumber

def countcharacters(list_of_strings):
    char_count = 0
    for i in list_of_strings:
        char_count += len(i)
    return char_count

# romannumerals stores all strings from roman.txt
romannumerals = []

with open('roman.txt', 'r') as file:
    lines = file.readlines()
    for l in lines:
        romannumerals.append(l.strip('\n'))
    file.close()

minimalromannumerals = []
for valid_roman in romannumerals:
    given_number = readromans(valid_roman)
    try:
        minimalromannumerals.append(efficient(validromans(given_number)))
    except:
        print given_number
        break

print countcharacters(romannumerals) - countcharacters(minimalromannumerals)
#print time()-t_0

'''
number = 500
print validromans(number)
print efficient(validromans(number))
'''

# times:
# (1) 0.011573 
