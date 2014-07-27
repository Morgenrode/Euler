'''prob8.py: find the 13 adjacent digits from a 1000-digit number with the largest product.'''

def prod(iterable):
         p = 1
         for n in iterable:
                  p *= int(n)
         return p


with open('input.txt', 'r') as f:
         x = f.read()
         x = ''.join(x.splitlines())

start = 1
end = 14
product = 1
while end <= 1001:
         block = x[start:end]
         if prod(block) > product:
             product = prod(block)
         else:
                  pass
         start += 1
         end += 1

print(product)
