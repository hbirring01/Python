#Dictionaries use key value pairs

students = {'Alice':25, 'Bob':27, 'Chris':17, 'Dan':21, 'Emma':22}

#Look up a value

print(students['Dan'])

#Add 

students['Fred'] = 25

#Modify

students['Alice'] = 26 

#Delete

del students['Fred'] 

#Get keys 

students.keys()

#This returns dict_keys data type, you cant index it but, it is iterable. You cant pick one out like students.keys()[0] you have to convert it to a list

A = list(students.keys())

A[2]

students.values()

#Dictionary does not have an order, you can only use the key to access an item and not the index

