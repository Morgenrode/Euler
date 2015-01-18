import itertools as it

count = 1
for n in it.permutations(range(10), 10):
    if count == 1000000:
        print(n)
    count += 1
    
