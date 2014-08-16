'''prob17: if all the numbers from 1 to 1000 were written out, how 
many letters would be used? No spaces or hyphens.'''

nums_to_words = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
    5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 
    10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 
    14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 
    18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 
    40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 
    80: 'eighty', 90: 'ninety', 100: 'onehundred', 
    200: 'twohundred', 300: 'threehundred', 400: 'fourhundred', 
    500: 'fivehundred', 600: 'sixhundred', 700: 'sevenhundred', 
    800: 'eighthundred', 900: 'ninehundred', 1000: 'onethousand'}

words = []
for i in range(1,1001):
    if i < 21:
        words.append(nums_to_words[i])
    elif i % 100 == 0:
        words.append(nums_to_words[i]) #100, 200, ... , 1000
    elif 1 <= i % 100 < 21:
        words.append(nums_to_words[int(repr(i)[0]) * 100] + 'and' +
            nums_to_words[int(repr(i)[1:])])
    elif i % 100 >= 21:
        if i < 101:
            words.append(nums_to_words[int(repr(i)[0]) * 10] + 
            nums_to_words[int(repr(i)[1])])
        else:
             words.append(nums_to_words[int(repr(i)[0]) * 100] + 'and' +
                nums_to_words[int(repr(i)[1]) * 10] + 
                nums_to_words[int(repr(i)[2])])
print(words)
print(len(''.join(words)))


