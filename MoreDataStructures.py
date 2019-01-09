#Combine multiple data types in a dictionary

students = {
    'Alice':['ID0001', 26, 'A'], 
    'Bob':['ID0002', 27, 'B'], 
    'Claire':['ID0003', 17, 'A'], 
    'Dan':['ID0004', 28, 'C'], 
    'Emma':['ID005', 27, 'A']
    }

print(students['Claire']) #Gives all of claires data 
#['ID0003', 17, 'A']

#Get just her id

print(students['Claire'][0])
#ID0003

#Give each key a dictionary value so we dont have to remember the order 

students2 = {
    'Alice':{'ID':'ID0001', 'Age':26, 'Grade':'A'},
    'Bob':{'ID':'ID002', 'Age':25, 'Grade':'B'},
    'Claire':{'ID':'ID003', 'Age':27, 'Grade':'C'},
    'Dan':{'ID':'ID004', 'Age':28, 'Grade':'D'},
    'Emma':{'ID':'ID005', 'Age':29, 'Grade':'E'}
    }

print(students2['Alice'])
#{'ID': 'ID0001', 'Age': 26, 'Grade': 'A'}

#Get Dan's Age
print(students2['Dan']['Age'])
#28 

#Retrieve Claire's ID and Grade

print(students2['Claire']['ID'], students2['Claire']['Grade'])
#ID003 C


