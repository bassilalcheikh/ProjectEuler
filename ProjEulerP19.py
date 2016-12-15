# Project Euler Problem #19: Counting Sundays
#
# How many Sundays fell on the first of the month during the twentieth century
# (1 Jan 1901 to 31 Dec 2000)?
#
# years
# months
# weeks
# days
#
days_count = (365*100+25)
days_index = [0]*(days_count)

def generate_first_of_months(year):
    standard_year = [1, 32, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
    leap_year = [1, 32, 61, 92, 122, 153, 183, 214, 245, 275, 306, 336]
    year_indeces = []
    if year%4 == 0: # leap year
        for i in range(0,366):
            if i in leap_year:
                year_indeces.append(1)
            else:
                year_indeces.append(0)
    else: # regular year
        for i in range(0,365):
            if i in standard_year:
                year_indeces.append(1)
            else:
                year_indeces.append(0)
    return year_indeces

for i in range(5,days_count,7):
    days_index[i] += 1

print(sum(days_index))

# Month| STD | Leap
# -----|-----|-----
# Jan  |   1 |   1
# Feb  |  32 |  32
# Mar  |  60 |  61
# Apr  |  91 |  92
# May  | 121 | 122
# Jun  | 152 | 153
# Jul  | 182 | 183
# Aug  | 213 | 214
# Sep  | 244 | 245
# Oct  | 274 | 275
# Nov  | 305 | 306
# Dec  | 335 | 336
