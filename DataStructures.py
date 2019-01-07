#Lists
"""
Create a list by using square brackets

mylist = [1, 2, 3, 4, 5]

"""

mylist = [1, 'Test', 0, True, False, 3, 'Test2']

#Lists are iterable and can be broken up, and each element can be accessed. Lists can have multiple data types in them 

if __name__ == "__main__":
    print(mylist)

    #Print 'True' from the list
    print(mylist[3])

    #To take out more than one element you need to use a slice 

    #mylist[start:end not including:step]

    print(mylist[0:3])

    #Lists can have other lists inside them

    mylist = [1,2,[3,4,5], 6, 7, 8]
    #Print the first index of the second list 
    print(mylist[2][0:])
    #Lists in lists are used in order to create tables 

    mytable = [[1,2,3], [4,5,6], [7,8,9]] 
    print(mytable[0][1])

    #Slices dont modify the lists in any way, they just take copies and modify the copy

    


