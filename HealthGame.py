import random

def health_potion(difficulty):
    health = 50 
    if difficulty == 1:
        new_health = random.randint(25, 50)
    elif difficulty == 2:
        new_health = random.randint(10, 25)
    elif difficulty == 3:
        new_health = random.randint(1, 10)
    health = print('new health is: ' + str(new_health))
    
    return(health)


if __name__ == '__main__':
#Passing in a different level (1 to 3) into the function will determine your new health.
    health_potion(1)

    