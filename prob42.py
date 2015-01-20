'''prob42: with letters corresponding to their alphabetical position,
find how many words in a given list are "triangle" words'''

import string
encoding = dict(zip(string.ascii_uppercase, [ord(c) % 32 \
    for c in string.ascii_uppercase]))

word_vals = []
with open('words.txt', 'r') as f:
    for word in f.read().split(','):
        word_vals.append(sum(\
        [encoding[c] for c in word.strip('\"')])) 

triangles = set()
n = 1
while ((n*(n + 1)) // 2) <= max(word_vals):
    triangles.add(int((n*(n + 1)/2)))
    n += 1

counter = 0
for i in word_vals: 
    if i in triangles:
        counter += 1

print(counter)


