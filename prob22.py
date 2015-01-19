'''prob22: sort a list into alphabetical order, treat each character 
in each string as an integer equal to its position in the alphabet, 
and find the total sum of all sums of character values * position 
in the list'''
import string

# ord(c) % 32 yields alphabetic position
encoding = dict(zip(string.ascii_uppercase, [ord(c) % 32 \
    for c in string.ascii_uppercase])) 

names = []
# the file is small, so read() on the whole thing isn't a huge deal
with open('names.txt', 'r') as f:
    for name in sorted(f.read().split(',')):
        names.append(name)

final_sum = 0
count = 1
for name in names:
   final_sum += (sum(encoding[c] for c in name.strip('\"')) * count) 
   count += 1

print(final_sum)
