'''prob19: how many sundays fell on the first of the month from 
1 jan 1991 to dec 31 2000'''

days = {0: 'sun', 1: 'mon', 2: 'tue', 3: 'wed', 4: 'thu', 5: 'fri', 
    6: 'sat'}

months = {'jan': 31, 'feb': 28, 'mar': 31, 'apr': 30, 
    'may': 31, 'jun': 30, 'jul': 31, 'aug': 31, 'sep': 30, 
    'oct': 31, 'nov': 30, 'dec': 31}

mons = ('jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 
    'sep', 'oct', 'nov', 'dec')

sundays = 0
year = 1901
day = 2 #jan 1 1901 was a tuesday
while year <= 2000:
    for mon in mons:
        if not (mon == 'feb' and year % 4 == 0):
            day = (day + months[mon]) % 7
        else:
            day = ((day + 29) % 7) 
        
        if day == 0:
            sundays += 1
        
    year += 1

print(sundays)

# this is kind of ugly, and worked well because jan 1 2001 was not a
# sunday, since this technically calculates the first of the NEXT
# month in the loop. But it worked!
