#Email slicer project

#Get the user email address

email = input('What is your email address?').strip() 

#Slice out user name

username = email[:email.index("@")]

#Slice domain name

doamin = email[email.index("@") + 1:]

#Format output message
output = 'your username is {} and your domain is {}.'.format(username,domain)

#Display output message
print(output)