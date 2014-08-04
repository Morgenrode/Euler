'''prob9.py: find the pythagorean triple s.t. a**2 + b**2 = c**2, a + b + c = 1000. Then, find 
the product a * b * c. Uses Dickson's method for finding triples.'''

def factPairs(square):
    factors = []
    for i in range(1, int(square**0.5 +1)):
        if square % i == 0:
            factors.append([i, square//i])
    return factors

possible = []
r = 2
numIters = 1
while numIters <= 167: # a < b < c, a + b + c = 1000, no way this can be over 334.
    for pair in factPairs((r**2)//2):
        possible.append([r + pair[0], r + pair[1],  r + pair[0] + pair[1]])
    r += 2
    numIters += 1

for i in possible:
    if sum(i) == 1000:
        print(i, i[0]*i[1]*i[2])

