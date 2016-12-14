# Project Euler Problem #19: Counting Sundays
#
# How many Sundays fell on the first of the month during the twentieth century
# (1 Jan 1901 to 31 Dec 2000)?
#
# years
# months
# weeks
# days

# January 1st, 1901 was a TUESDAY  .... January 6th, 1901 was a SUNDAY
# December 31st, 1901 was a TUESDAY

# January 1st, 1953, was a THURSDAY
# December 31st, 1953, was a THURSDAY

# January 1st, 1960, was a FRIDAY
# December 31st, 1960, was a SATURDAY

days_count = (365*100+25)
days_index = [0]*(days_count)

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
