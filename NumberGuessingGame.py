#This is a twist on the classic number game

import random

print("Hello, My name is Computer 1. What is your name?")
#Computer Name

print("Well, <name>, I am thinking of a number between 1 and 20")
print("You will have 6 guesses.")

#Selecting a random number between 1 and 20
secretNumber = random.randint(1, 20)
print(f"DEBUG:The secret number is : {secretNumber}")

for guessesTaken in range(1, 7): #or range(7)
    print("Take a guess.")
    userGuess = int(input())

    if userGuess > secretNumber:
        print("Your guess is too high")
    elif userGuess < secretNumber:
        print("Your guess is too low")
    else:
        break

if userGuess == secretNumber:
    print(f"Yes! You got it in, {guessesTaken} moves. ")
else:
    print(f"Nope, The number was {secretNumber}")

#for key in range(random.randInt(2, 10)):
 #   name = 



