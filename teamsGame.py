# william black
# 2/1722
#learn strings and several functions

import os, random
os.system('cls')

print('choose a game')

print('animals (1)')
print('pc parts (2)')
print('fruits (3)')
gamechoice=input('choose a game')
#list
animallist=["monkey",'dog', 'cat', 'cow']
fruitlist=["banana", "apple", "plum", "mango"]
pclist=['cpu','gpu','ram','mobo']

def guessFun():
    global guess
    check=True
    while check:
        try:
            guess=input('enter a letter')
            if guess.isalpha():
                check=False
            else:
                print('please only enter letters')
        except ValueError:
            print('please only enter letters')

def playgame():
    global gameOn
    os.system("cls")
    answer=input("do you wanna play again")
    if 'n' in answer.lower:
        gameOn=False

def selWord():
    global word
    if gamechoice==1 :
        word=random.choice(animallist)
    elif gamechoice==2:
        word.random.choice(pclist)
    elif gamechoice==3:
        word.random.choice(fruitlist)


while gameOn:
    guessFun()
    letterGuessed+=guess #letterguessed=letterguessed+guess     
    if guess not in word:
        counter+=1
        print(counter)
    for letter in word:
        if guess in word:
            guessedLetter +=1
        if letter in letterGuessed:
            print(letter, end=' ')
        else:
            print("_", end=' ')
            counter+=1
    if counter>6:
        print ('you lost')
        playgame()
    if guessedLetter == len(word):
        print('you won')



    