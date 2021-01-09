import random
#We chose to allow the players to only choose the higher bound to avoid having a negative lower bound.
ChooseHigherBound = int(input("Choose an ending number for your range. Please choose a number above 1. "))
number = random.randint(1,ChooseHigherBound)
ChooseNumber = int(input("Choose a number within your chosen range: "))
while ChooseNumber != number:
    if number > ChooseNumber:
        print("Incorrect. The number is higher. Guess again!")
    elif number < ChooseNumber:
        print("Incorrect. The number is lower. Guess again!")
    elif type(ChooseNumber) != int:
        print("Error. Only integers are allowed. Guess again!")
    ChooseNumber = int(input("Please try again: "))
print ("Congratulations! You guessed the number!")