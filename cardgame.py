import random, os
gameOn = True
os.system('clear')
deck=[]
#next, let's start building lists to build the deck
#NumberCards is the list to hold numbers plus face cards
numberCards = []
suits = ['♥',"♦", "♣", "♠️"]
royals = ["J", "Q", "K", "A"]
def menu():
    global gameOn
    print(' _________________________________________________________ ')
    print('|                           WAR                           |')
    print('|    Welcome to war, please read the directions first:    |')
    print('|=========================================================|')
    print('| Objective:                   | Set-Up:                  |')
    print('|   -Collect all of the cards  |   -2 Players             |')
    print('|    before the opponent       |   -26 Cards a hand       |')
    print('|=========================================================|')
    print('| -How to play: 1) Both players will "place their card    |')
    print('|down" at the exact same time, their card being anonymous |')
    print('|anonymous to their opponent. 2) The cards are revealed at|')
    print('|at the same time, whomever places the highest valued card|')
    print('|keeps both cards which then goes into the players discard|')
    print('|pile. Once a player looses their whole hand they will    |')
    print('|then turn their discard pile into their new hand. The    |')
    print('|first player to loose both their original hand, and their|')
    print('|discard pile looses.|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|')
    input(' ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯| Are you ready to play (Y|N)        |')
    print('                     |____________________________________|')      

def WarMenu():
    print('__________________________________________________________')
    print('| Heres ther good part, it looks like you and the other   |')
    print('|player have both placed the same card. THIS IS WAR       |')
    print('|=========================================================|')
    print('|Both, you and your opponent will place 3 anonymous cards |')
    print('|down ontop of the original, mathcing card. the last      |')
    print('|placed card will then be revealed, and whomever placed   |')
    print('|the highest valued card, claims all for cards. If the new|')
    print('|last placed cards are identical, again, there will be    |')
    print('|another war. Have Fun!|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|')
    input(' ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯| Are you ready for war? (Y|N)     |')
    print('                       |__________________________________|')    

menu()

#using loops and append to add our content to numberCards :
for i in range(2,11):
    numberCards.append(str(i))
    #this adds numbers 2-10 and converts them to string data

for j in range(4):
    numberCards.append(royals[j])
    #this will add the card faces to the base list
#Create full deck
for k in range(4):   # four suits
    for l in range(13): #13 cards per suit
        card = (numberCards[l] + " " + suits[k])
        #this makes each card, cycling through suits, but first shows face
        deck.append(card)
        #this adds the information to the "full deck" we want to make
#you can print the deck here, if you want to see how it looks

#now let's see the deck!
counter=0
for row in range(4):
    for col in range(13):
        print(deck[counter], end=" ")
        counter +=1
    print()
#now let's shuffle our deck!
#Shuffle the deck cards
random.shuffle(deck)
player1=[]
player2=[]
# you could print it again here just to see how it shuffle
#loop to devide the cards to each player
for l in range(52):
    if l%2==0:
        player1.append(deck[l])
    else:
        player2.append(deck[l])

halfDeck=int(len(deck)/2)
plyr1=0
plyr2=0

    #ask user to hit a key to release cards

for i in range (0,halfDeck):
    click=input("Press any key to get cards")
    print("Player 1     Player 2")
    print("     "+player1[i]+"      "+player2[i])
    
    if player1[i]>player2[i]:
        plyr1 +=1
        print("Player I: "+str(plyr1)+"     Player II: "+ str(plyr2))
    elif player1[i]<player2[i]:
        plyr2 +=1
        print("Player I: "+str(plyr1)+"     Player II: "+ str(plyr2))
    elif player1[i]==player2[i]:
        WarMenu()

if plyr1>plyr2:
    print("Player one won the game "+str(plyr1)+" to "+str(plyr2))
elif plyr2>plyr1:
    print("Player two won the game "+str(plyr2)+" to "+str(plyr1))
