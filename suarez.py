#MariaSuarez 
# 02/08/2022
def menu():
    global choice
    print('## Word game with 3 levels ##') 
    print('## 1. Fruits ##')
    print('## 2. Animals ##')
    print('## 3. Computer Parts ##')
    choice=print('## choice ##')
    check=True
    while check:
        try:
            choice=int(input("## Enter a choice ##"))
            if choice>0 and choice<4:
                check=False
            else:
                print('## number 1-3 please ##')
        except ValueError:
            print("## number 1-3 please ##")

#Create word lists
import os, random
os.system('cls')
word=""
guess=""
def selectWord():
    global word
    fruits=["bananas", "grapes", "waterMelon", 'blueberries', 'apples', "blackberries",
    "papaya", 'oranges', 'tomatoes', 'mangos', 'kiwis','strawberries' ]

    if choice==1:
        word=random.choice(fruits)
    elif choice==2:
        word=random.choice(animals)
    else:
        word=random.choice(pclist)
    for letter in word:
        print('_', end=' ')



def guessFunction():
    global guess
    check=True
    while check:
        try:
            guess=input("\nenter a letter to guess the word ")
            if guess.isalpha() and len(guess)==1:
                check=False
            else:
                print("only one letter please")
        except ValueError:
            print("only one letter please")

def playagain():
    global gameOn
    global score
    global tries
    global letterGuessed
    os.system("cls")
    againchoice=input("do you wanna play again")
    if againchoice=='y':
        menu()
        selectWord()
        score=0
        tries=0
        letterGuessed=''   
    else:
        print('your high score was')
        print(highscore)
        gameOn=False

        

gameOn=True
tries=0
letterGuessed=""
menu()
selectWord()
print()
highscore=0
while gameOn:
    
    guessFunction()
    letterGuessed += guess  #letterGuessed=letterGuessed + guess
    if guess not in word:
        tries +=1
        print(tries)# for testing delete when game is ready
    countLetter=0
    for letter in word:
        if letter in letterGuessed:
            print(letter, end=" ")
            countLetter +=1
        else:
            print("_", end=" ")
    if tries >6:
        print("\n Sorry run out chances ")
        playagain() #ask if they want to play again
    if countLetter == len(word):
        print ("\nyou guessed! ")
        score=len(word)*5-2*tries
        if score>highscore:
            highscore=score
        #Calculate score
        playagain()

