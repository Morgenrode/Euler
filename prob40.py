'''prob40.py: Champernowne's constant. if d_n represents the nth
digit of the number formed by the concatenation of integers, find 
the value of d_1 x d_10 x ... x d_1000000'''

num = ''.join([str(i) for i in range(1000000+1)])

prod = int(num[1])
for i in range(1,7):
    prod *= int(num[10**i])

print(prod)

