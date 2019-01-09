Films = {
    'Finding Dory':[3,5],
    'Bourne':[18,5],
    'Tarzan':[15,5],
    'Ghost Busters':[12, 5]
}
while True:
    choice = input('What film would you like to watch?').strip().title()
    if choice in Films:
        age = int(input('What is your age?').strip())
        if age >= Films[choice][0]:
            if Films[choice][1] >= 1:
                print('Enjoy the film!')
                Films[choice][1] = Films[choice][1] - 1 
            else:
                print('We dont have enough seats left')
        else:
            print('You are too young for this film')
    else:
        print('We dont have that film')
    