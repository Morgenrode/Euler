'''prob13: find the first 10 digits of the sum of one-hundred 50-digit numbers'''
#This still feels dirty. Python3 ints behave as longs by default.

numbers = []
with open('input.txt', 'r') as f:
    for line in f.readlines():
       numbers.append(line.rstrip('\n'))
x = 0
for i in numbers:
    x += int(i)

print(x)

