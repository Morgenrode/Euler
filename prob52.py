'''prob52.py: Permuted Multiples
find the least pos int x | 2x, 3x, 4x, 5x, 6x contain the same 
digits as x'''
import math as m

def int_set(i):
    '''This function breaks an integer i into a set containing the digits of i'''
    x = set([(i % 10**n)//10**(n-1) for n in range(1, (m.ceil(m.log10(i))) + 1)])
    return x

i = 1
while True:
    #only continue if i and 6i have the same number of digits
    if (6*i) <= 10**(m.ceil(m.log10(i))):
        if int_set(i) == int_set(2*i) == int_set(3*i) == int_set(4*i) == int_set(5*i) == int_set(6*i):
            print(i)
            break
    i += 1
