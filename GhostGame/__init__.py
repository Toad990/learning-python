# ghost game
from random import randint
print ('Ghost game')
feeling_brave = True
score = 0
while feeling_brave:
    ghost_door = randint (1, 3)
    print (ghost_door)
    print('three doors ahead')
    print(' A ghost behind one')
    print (' which door do you open ?')
    door = input('1 ,2 ,3?')
    door_num = int (door)
    if door_num == ghost_door:
        print ("GHOST !")
        feeling_brave = False
    else:
        print (' no ghost!')
        print ('you enter the next room')
        score = score + 1
print ('RUN AWAY !')
print (' Game over! you scored', score)






