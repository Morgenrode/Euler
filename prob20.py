'''prob20: find the sum of the digits in the number 100!'''
# This kind of trivializes the problem
import math

x = str(math.factorial(100))
total = [ int(i) for i in x ]
print(sum(total))
