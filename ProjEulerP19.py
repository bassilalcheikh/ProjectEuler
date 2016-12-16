# Project Euler Problem #19: Counting Sundays
#
# How many Sundays fell on the first of the month during the twentieth century
# (1 Jan 1901 to 31 Dec 2000)?
#
from time import time

t_0 = time()
def generate_sundays(years_quantity):
    days_count = int(years_quantity*(365.25))
    days_index = [0]*days_count
    for i in range(5,days_count,7):
        days_index[i] += 1
    return days_index

def generate_first_of_years(years_quantity): #enter years_quantity divisible by 4
    new_years_days = []
    # every 1461 days, we begin a new cycle
    total_days = int(365.25*years_quantity)
    # [0, 365, 730, 1095]
    for i in range(0, total_days, 1461):
        for j in range(0,4):
            new_years_days.append(i+j*365)
    return new_years_days

all_new_years = generate_first_of_years(100)

standard_year = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
leap_year = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]

set_of_days = []
for i in all_new_years:
    if i%4 == 0:
        for j in leap_year:
            set_of_days.append(i+j)
    else:
        for k in standard_year:
            set_of_days.append(i+k)

sundays = generate_sundays(100)

counter = 0
for i in set_of_days:
    if sundays[i] == 1:
        counter +=1
t_1 = time()
print(counter)

print(t_1-t_0)

# times:
# 0.00146508216858 seconds
