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
userNum = input ('choose game: ')
if userNum==1 :
    guess=random.randint (1,10)
    userguess=input
    if userguess == guess :
        print ('you won :)')
    else :
     ('incorrect :(')