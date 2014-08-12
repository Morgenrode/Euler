'''prob16: sum of the digits of 2^1000'''
#This feels like cheating, python will use longs
#without any extra thought

x = str(2**1000)
print(sum([int(i) for i in x]))
