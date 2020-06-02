#This is a twist on the classic number game
#Here a computer itself tries to guess the number guessed by the computer
#using trial and error

import random

print("Computer: Hello, My name is Computer. What is your name?\n")

#Computer Name
#Creating a random name using the alphabets 
#Adding the alphabets to the empty lists
#and assigning the name using random() functions
computerName = ""
alphabetList = []

for i in range(97, 123):
  alphabetList.append(chr(i))

for key in range(random.randint(1, 10)):
    j = random.randint(0, 25)
    nameCharacter = alphabetList[j]
    computerName = computerName + nameCharacter

print(f"{computerName}: Hello, Computer. My name is {computerName}\n")

print(f"Well, {computerName}, I am thinking of a number between 1 and 20")
print("You will have 6 guesses.\n")

#Selecting a random number between 1 and 20
secretNumber = random.randint(1, 20)

#Computer Guessing:
computerList = [i for i in range(1, 21)]
low = computerList[0]
high = computerList[19]

guessesTaken = 1

while guessesTaken != 6:
  mid = (low + high)// 2
  print("Take a guess.")
  computerGuess = mid

  if computerGuess > secretNumber:
    print(mid)
    print("Your guess is too high")
    high = mid - 1
    mid = (low + high)// 2

  elif computerGuess < secretNumber:
    print(mid)
    print("Your guess is too low")
    low = mid + 1
    mid = (low + high)// 2

  else:
    print(mid)
    break

  guessesTaken = guessesTaken + 1 


if computerGuess == secretNumber:
    print(f"Yes! You got it in, {guessesTaken} moves. ")
else:
    print(f"Nope, The number was {secretNumber}")









