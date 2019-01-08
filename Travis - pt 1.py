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
            print('No problem I didnt remove you from the system!')

    else:
        print('I dont think I have met you yet {}'.format(name))
        add_me = input('Would you like me to add you to the system {}? (y/n)'.format(name)).lower().strip()
        if add_me == 'y':
            known_users.append(name)
        elif add_me == 'n':
            print('No problem I will not add you to the system')
            


#to remove specific indexes do del list[index]
