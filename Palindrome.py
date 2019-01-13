tocheck = input('Enter a word to see if it is a palindrome: ').strip().lower() 

reverse = tocheck[::-1]

if reverse == tocheck:
    print('{} is a palindrome'.format(tocheck))
else:
    print('{} is not a palindrome'.format(tocheck))
