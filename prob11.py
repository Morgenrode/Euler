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

j = 0
while j < 20:
    i = 0
    while i < 20:
        # Straight line path, left-to-right
        try:
            if prod(grid[j][i:i+4]) > product:
                product = prod(grid[j][i:i+4])
        except:
            pass
        # Straigh path, top-to-bottom
        try:
            if prod([grid[j][i], grid[j+1][i], \
            grid[j+2][i], grid[j+3][i]]) > product:
                product = prod([grid[j][i], grid[j+1][i], \
            grid[j+2][i], grid[j+3][i]])
        except:
            pass
        print(product)
