known_users = ['Alice', 'Bob', 'Claiare', 'Dan', 'Emma', 'Fred', 'Georgie', 'Harry']

while True:
    print('Hi my name is Travis')

    name = input('What is your name? ').strip().capitalize()

    if name in known_users:
        print('Hello {}!'.format(name))
        remove = input('Would you like to be removed from the system? (y/n)').lower().strip()
        if remove == 'y':
            known_users.remove(name)
            print('{} has been removed!'. format(name))

    else:
        print('Name NOT recognized')

#to remove specific indexes do del list[index]
