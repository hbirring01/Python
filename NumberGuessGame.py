from random import randint
CPUSelection = randint(1, 100)

PlayerSelection = int(input('Pick a number').strip()) 
KeepGuessing = True

while KeepGuessing == True:
    if PlayerSelection > CPUSelection:
        print('You guessed too high')
    elif PlayerSelection < CPUSelection:
        print('You guessed too low')
    elif PlayerSelection == CPUSelection:
        print('You guessed the number! It was {}'.format(CPUSelection))
        break 


