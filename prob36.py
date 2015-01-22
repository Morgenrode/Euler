'''prob36: Double-base palindromes:
find the sum off all numbers < 1,000,000, which are 
palindromic in base 10 and 2'''

print(sum([i for i in range(1, 1000000 + 1) if (str(i) == str(i)[::-1]) and (bin(i)[2:] == bin(i)[-1:1:-1])]))
