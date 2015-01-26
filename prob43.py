'''prob43: pandigitals of [0..10] with substring divisibility
suppose x = 1234567890; then d_2d_3d_4 = 234, &c. we want the total 
number of 10-digit panditigals with the following sub-divisibility:
d_2d_3d_4 % 2 == 0, d_3d_4d_5 % 3 == 0, ... , d_8d_9d10 % 17 == 0;
i.e., divisibility by successive prime numbers'''
import itertools

numbers = itertools.permutations(range(10), 10)

pandigitals = []
modulos = [17, 13, 11, 7, 5, 3, 2]
divisors = [10 ** i for i in range(7)]

def compare(num, mods, divs):
    if all(((num // div) % 1000) % mod  == 0 for mod, div in zip(mods, divs)):
        return True
    else:
        return False
        
for num in numbers:
    num = int(''.join([str(i) for i in num]).zfill(10))
    if compare(num, modulos, divisors):
        pandigitals.append(num)
    

print(sum(pandigitals))
