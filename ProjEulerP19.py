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
