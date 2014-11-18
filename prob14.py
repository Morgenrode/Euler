"""prob14.py: Which starting number, under 1,000,000, gives the 
longest chain of terms following the Collatz sequence. 
n -> n/2 if n is even, n -> 3n + 1 if n is odd
uses a cache to keep from performing repeated calculations, as 
the brute-force approach exceeded 2 minutes on my old laptop"""

max_chain = 0
max_chain_number = 0
cache = {1:1}

for i in range(1,1000001):
    counter = 0
    j = i
    while i != 1 and i >= j:
        if i % 2 == 0:
            i /= 2
        else:
            i = 3*i + 1
        counter += 1
    cache[j] = counter + cache[i]
    if cache[j] > max_chain:
       max_chain = cache[j]
       max_chain_number = j

print(max_chain_number)
