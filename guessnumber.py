import os
import random
os.system ('cls')
# --> is for comments
# William Black
# 01/20/22
# create random number, give user a hint if number is even or odd, ask user for guess, 
# compare numbers, print you won or you lost 
gameOn=True
counter=0
#get number from random
guess = random.randint (1,20)
#give hint
if guess%2 == 0 :
    print ('the number is even')
else:
    print ('the number is odd')
while gameOn :
    #get number from user
    userNum = input ('guess a number 1-20 ')
    counter= counter+1
    #check if user guessed the number
    userNum=int(userNum)
    if userNum == guess :
        print ('you won')
        gameOn=False
    else:
        if userNum > -10:
            print ('you are too far up')
        else:
            if userNum < guess-10:
                print('you are too far high')
    if counter==5 : 
        print ('you lost')
        gameOn = False
    
    #make sure that if you are indenting, you add a : at the end
    #make sure that you use a comma with numbers, not dash (check line 10)
    #make sure that the order is correct 
