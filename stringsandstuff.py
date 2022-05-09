
# william black
# 2/1/22
#learn strings and several functions

import os, random
os.system('cls')
schoolName="Greenhill School"
schoolName=schoolName.upper()
print(len(schoolName))
lastCharacter= len(schoolName)-1
print(schoolName)
if "g" in schoolName:
    print("There is a blank in the word")
letter= random.choice(schoolName)
print(letter)
gameOn=True
while gameOn:#Main game loop
    #Loop to check user input
    check = True
    while check:
        try:
            userInput=input("Guess the letter I am thinking of ").upper()
            print(userInput)
            if userInput.isalpha() : #if you need to include numbers use is alnum
                check = False
        except ValueError:
            print("sorry, only letters please ")
    if userInput == letter:
        print("you guessed it")
        gameOn=False
    elif userInput in schoolName:
        print("the letter is in the word I am thinking of")
    for i in range(len(schoolName)):
        print(schoolName[i])

        