#This is a twist on the classic number game

import random

print("Computer: Hello, My name is Computer. What is your name?\n")

#Computer Name
computerName = ""
alphabetList = []
for i in range(97, 123):
  alphabetList.append(chr(i))


for key in range(random.randint(2, 10)):
    i = random.randint(1, 26)
    nameCharacter = alphabetList[i]
    computerName = computerName + nameCharacter

print(f"{computerName}: Hello, Computer. My name is {computerName}")

print(f"Well, {computerName}, I am thinking of a number between 1 and 20")
print("You will have 6 guesses.")

#Selecting a random number between 1 and 20
secretNumber = random.randint(1, 20)
#print(f"DEBUG:The secret number is : {secretNumber}")

#Computer Guessing:
computerList = [i for i in range(1, 21)]
low = computerList[0]
high = computerList[19]
 #mid = (low + high)// 2
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









