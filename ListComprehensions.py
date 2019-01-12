even_numbers = [x for x in range(1, 101) if x % 2 ==0]
print(even_numbers)

"""
first x in the statement is what is going to be stored in the list
second x in the statement represents every number that is looped through even the odd ones(1-100)
if the remainder of x divided by 2 is 0 then we keep it in the list, if not we discard it.
[ expression for item in list if conditional ] 

new_list = [expression(i) for i in old_list if filter(i)]
new_list    
The new list (result).

expression(i)
Expression is based on the variable used for each element in the old list.

for i in old_list
The word for followed by the variable name to use, followed by the word in the
old list.

if filter(i)
Apply a filter with an If-statement.
"""
words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the ', 'lazy', 'dog']
answer = [[w.upper(), w.lower(), len(w)] for w in words]

Even = [x for x in range(1, 101) if x % 2 == 0]