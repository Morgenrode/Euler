'''prob12: find the first triangle number with over 500 divisors. A triangle number is 
formed by sequential addition of the natural numbers.'''

def factorNumber(num):
	factors = 0
	for i in range(1, int(num**0.5 +1)):
		if num % i == 0:
			factors += 1
	return factors 

numDivisors = 0
x = 1
i = 2
while numDivisors < 500:
	x += i
	if factorNumber(x) > numDivisors:
		numDivisors = factorNumber(x)
	
	print(x)
	i += 1
print(x)
