'''prob81: find the minimal path sum from TL to BR of an 
80x80 matrix. Only movement down or right is allowed.'''

grid = []

# This makes grid an 80 element list of lists with 80 integers as their elements
with open('matrix.txt', 'r') as f:
	for line in f.readlines():
		numline = []
		for block in line.split(','):
			numline.append(int(block))
		grid.append(numline)

