'''prob10.py: find the sum of all the primes below two million. Uses 
an implementation of the Sieve of Eratosthenes'''
bools = [True for i in range(0, 2000001)]

for i in range(2,(int(2000000**0.5) + 1)):
    if bools[i]:
        j = i**2
        while j < 2000001:
            bools[j] = False
            j += i

print(sum([i for i in range(2,2000001) if bools[i]]))
