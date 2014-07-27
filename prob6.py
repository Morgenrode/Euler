'''prob6.py: find the difference between the sum of the squares of the first 100 natural numbers and the square of the sum'''

sum_of_squares = sum([x ** 2 for x in range(1,101)])
square_of_sum = (sum([x for x in range(1,101)]))**2

print(sum_of_squares - square_of_sum)

