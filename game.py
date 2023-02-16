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
random_number = randint(10,50)

counter = 0
while counter < 5:
    user_number = eval(input("Enter a number: "))
    counter += 1

    if user_number < random_number:
        print("Your guess is too low.")
    elif user_number > random_number:
        print("Your guess is too high.")
    elif user_number == random_number:
        break

if user_number == random_number:
    print("  YOU WIN!  ")
else:
    print("Game over.The correct number is...")
    print(  random_number  )









 