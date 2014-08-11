'''prob11: find the greatest product of 4 adjacent elements of a 
20x20 grid of numbers'''

def prod(iterable):
'''Simple function to find the product of the input elements'''
    p = 1
    for n in iterable:
        p *= int(n)
    return p

grid = []
product = 1

with open('input.txt', 'r') as f:
'''This makes every line in the input file a list of integers, and
appends that list into a bigger list, grid'''
    for line in f.readlines():
        line = line.replace(' ', ',').strip('\n')
        numline = []
        for block in line.split(','):
            numline.append(int(block))
        grid.append(numline) 

#try:
#    product = prod(listx[i]...etc
#except:
#    pass
