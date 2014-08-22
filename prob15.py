'''prob15: find the number of unique routes through a 20x20 grid, 
starting from the top left and going to the bottom right, with only 
movements down and right allowed at each node. Calculation was 
performed by hand, noting that each path required a total movement 
of 2n spaces, with n down and n right moves. Thus, the number of 
unique paths is 40!/(20! * 20!)'''

from math import factorial as f
print(f(40)/(f(20)*f(20)))
