'''prob12: find the first triangle number with over 500 divisors. A triangle number is 
formed by sequential addition of the natural numbers.'''
import time
start = time.time()
def factorNumber(num):
	factors = 0
	for i in range(1, int(num**0.5 +1)):
		if num % i == 0:
			factors += 2
	return factors 

numDivisors = 0
i = 1
while numDivisors < 500:
	x = (i*(i + 1))/2 # generate the triangle numbers
	if factorNumber(x) > numDivisors:
		numDivisors = factorNumber(x)
	i += 1
	print(x)	
	print(numDivisors)
end = time.time()
print(end - start)

'''took 8.92 seconds to find the answer.
had the idea of vectors containing the frist several primes and exponents, such as

primes = [2,3,5,7,11,13,...]
exponents = [1,1,1,1,1,1,...]

and making sure that 1*=(i+1) for i in exponents >= 500, and then checking if those numbers generated were
triangle numbers, but i did not implement it (yet)'''
