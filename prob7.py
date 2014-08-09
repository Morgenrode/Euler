'''prob7.py: find the 10001st prime number. Reuses code from prob10
for generating primes using the Sieve of Erat. TODO: rewrite so that
this generates primes, rather than calculates past the desired prime then
finds it by index'''
bools = [True for i in range(0, 2000001)]

#Finding all primes below 2M takes like, two seconds.

for i in range(2,(int(2000000**0.5) + 1)):
    if bools[i]:
        j = i**2
        while j < 2000001:
            bools[j] = False
            j += i

trueIndex = 0 #Keeps track of how many primes we've encountered
numIndex = 0 #Number of iterations
for i in bools[2:]: #first two elements were set to True initially
    if i:
        trueIndex +=1
        if trueIndex == 10001:
            print(range(2,2000001)[numIndex])
    numIndex += 1
