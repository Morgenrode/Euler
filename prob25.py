'''prob25.py: find the first fibonacci number with 1000 decimal digits'''

a,b = 1,1
term = 2
while b % 10**999 >= b: #once the number is 1000+ digits, the number mod 10**999 will be small
    a,b = b,a+b
    term += 1
print('Answer:', term)
