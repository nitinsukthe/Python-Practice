# ROCK PAPER SCISSORS
'''
1 for Rock
-1 for Paper
0 for Scissors
'''

import random
computer = random.choice([1, -1, 0])
youstr = input("Enter your choice: ")
youDict = {"r":1, "p":-1, "s":0}
reverseDict = {1:"Rock", -1:"Paper", 0:"Scissors"}

you = youDict[youstr]

print(f"You choce {reverseDict[you]}\n computer choce {reverseDict[computer]}")

if(computer == you):
    print("Its a draw")

else:
    if(computer == 1 and you == -1):
        print("You win!")
    elif(computer == 1 and you == 0):
        print("You lose")
    elif(computer == -1 and you == 1):
        print("You lose")
    elif(computer == -1 and you == 0):
        print("You win!")
    elif(computer == 0 and you == 1):
        print("You win!")
    elif(computer == 0 and you == -1):
        print("You lose")
    else:
        print("Somethhing went wrong")
