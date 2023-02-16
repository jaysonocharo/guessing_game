#This program demonstrates a guessing game.


#1-get user name
#2-generate a random number
#3-generate user number
#4- using a while loop,check if user input is equal to generated number.

from random import randint
#1
username = input("What is your name?: ")
print("Hello there "+username+"!")

#2-generate a random number
number = randint(10,50)

counter = 0
while counter < 5:
    usernumber = eval(input("Enter a number: "))






 