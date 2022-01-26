from mimetypes import guess_all_extensions
import os
import random
os.system ('cls')
# --> is for comments
# William Black
# 01/23/22
#print("#   Guess a number Menu     #")
# add a menu
# choices  1-10
# choices 1 -50
# choices 1-100
print ('')
print(' choose a game! ')
print ('')
print ('choose 1 for 1-10.')
print ('choose 2 for 1-50')
print ('choose 3 for 1-100')
guess=0
level=0
gameType=''
check=True
while check:
    gameType=input('select a game!')
    try:
        gameType=int(gameType)
        if gameType > 0 and gameType < 4:
            check=False
        print ('\nPlease enter a number 1-3')
    except ValueError:
        print ('wrong input... try again!')

def randomNum(gameType) :
    global level
    global guess 
    if gameType==1:
        guess=random.randint (1,10)
        level=10
        userGuess=input('\nguess a number 1-10')
        userGuess==guess 
        print('you win')
    else:
        print ('incorrect')
    if gameType==2:
        guess=random.randint (1,50)
        level=50
        userGuess=input ('\nguess a number 1-50')
        userGuess==guess 
        print('you win')
    else:
        print ('incorrect')
    
    if gameType==3:
        guess=random.randint (1,100)
        level=100
        userGuess=input ('\nguess a number 1-100')
        userGuess==guess 
        print('you win')
    else:
        print ('incorrect')
randomNum(gameType)

