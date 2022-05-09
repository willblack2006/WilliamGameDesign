from cgi import print_directory
from mimetypes import guess_all_extensions
import os
import random
os.system ('cls')
# --> is for comments
# William Black
# 01/23/22
#make a rock paper scissors game
#let the player choose first
def play():
    print ('*   Welcome!    *')
    print('Rock Paper Scissors ')
    print('     rock: r')
    print('     paper: p')
    print('     scissors: s')
    user=input('Enter your choice:') 
    user = user.lower()
    computer=random.choice(['r','p','s'])
    if user==computer:
        return ('its a tie :l').format()
    if win(user, computer):
        return ('you won :)').format(user, computer)
    return ('you lost :(')
def win(player, opponent):
    if (player== 'r' and opponent== 's') or (player=='s' and opponent == 'p') or (player== 'p' and opponent== 'r'):
        return True 
    return False
if __name__ == '__main__':
    print(play())