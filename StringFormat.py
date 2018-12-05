#Formatting Strings (String interpolation)
my_name = "Harman"
print("Hello my name is " + my_name)

#.format method

print("This is a string {}".format("INSERTED TEXT"))
print("The {} {} {}".format("quick", 'brown', 'fox'))
print("The {2} {1} {0}".format('quick', 'brown', 'fox'))
print("The {0} {0} {0}".format('quick', 'brown', 'fox'))

#assing keywords
print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick' ))

#float Formatting
result = 100/777
print(result)

print('The result was {r} '.format(r = result))

#float formatting is as follows "{value:width.percision f}"
print('The result was {r:2.10}'.format(r = 'result'))

#f-strings were introduced in python 3

name = 'Harman'
print(f'Hello his name is {name}')

name = 'Sam'
age = 3

print(f'name is {name} and age is {age}')
