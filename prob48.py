'''prob48: last 10 digits from the sum of 1**1 + 2**2 ... 1000**1000'''
print(sum([i ** i for i in range(1, 1001)]) % 10**10)

