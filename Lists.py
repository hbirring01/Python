A = [5,12,72,55,89]

#You can only add lists to lists or use append

A = A + [1]

#To add a string

A = A + ['bcd']

#Add a string to the list as its own element

A = A + list('BCD')

#Integers cannot be added that way because integers are not iterable unless you convert them to string

A = A + list(str(123))

#A.insert('index', 'object to insert')

