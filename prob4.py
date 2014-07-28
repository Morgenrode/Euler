'''prob4.py: find the largest palidrome made form the product of two 3-digit numbers'''

def isPalindrome(num):
         '''Test a string version of a number for palindromicity'''
         return str(num)[::-1] == str(num)

def search():
         '''Search through all combinations of products of 3 digit numbers'''
         palindrome = 0
         for x in range(100,1000):
                  for y in range(100,1000):
                           z = x * y
                           if isPalindrome(z) and z > palindrome:
                                    palindrome = z
                           else:
                                    pass
          
         return palindrome

print(search())
