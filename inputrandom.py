from mimetypes import guess_all_extensions
import os
import random
os.system('cls') 
# --> is for comments
# William Black
# 01/20/22
#learn user input
#learn other operators, %, **, random numbers, branching
#program will ask user to guess a number
#
# Declare variables : and use input() function
userInfo=input("Enter a number between 5 and 15: ")
print(userInfo)
print(type(userInfo))

#typecasting -- line below makes numbers add
userInfo=int(userInfo)
print(userInfo+34)
print(userInfo/2)
print(userInfo%2) #modulus operator (%) gives remainder instead of a decimal

if userInfo%2 == 0 : # if the number is even, because the remainder is 0
    print ("the number is even")
else: 
    print("the number is odd")

#create a random number
guess = random.randint(1,50)
print(guess)
