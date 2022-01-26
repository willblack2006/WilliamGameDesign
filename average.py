import os
# --> is for comments
# William Black
# 01/18/22
# Declare variable, print values, operators, type of data
# Program to calculate the average of 3 tests
# Declare variables :
test1=89
test2=78
test3=91.5
os.system('cls')
#to display results we use print
#calculate sum of tests
sum=test1+test2+test3
print ('this is the sum of the 3 tests' , end='=')
# jf we put '; end ='='it will stay on the same line, not return'
#calculate average

average=int((sum/3)*100)
print(average/100)
print (sum//3)
print ("the average of"+str(test1)+","+str(test2)+", and "+str(test3) + "is", end= '=')

# if the number is not a nice number (decimal) we can put 'int' and *100. Then divide it by 100 to get the 
# good number. double division (//) gets rid of the decimal, whereas rounding goes down/up.
#when we use one star (*) it is multiplication, when we use 2 stars (**) it multiplies to the power of.
print(2**3) # 2 to the power of 3
