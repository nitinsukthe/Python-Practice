# PROJECT 1
# SNAKE, WATER, GUN GAME
import random
computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice: ")
youDict = {"s":1, "w":-1, "g":0}
reverseDict = {1:"snake", -1:"water", 0:"gun"}

you = youDict[youstr]

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")


if(computer == -1 and you == 1):
    print("You win!")
elif(computer == -1 and you == 0):
    print("You Lose!")
elif(computer == 1 and you == -1):
    print("You Lose!")
elif(computer == 1 and you == 0):
    print("You win!")
elif(computer == 0 and you == -1):
    print("You win!")
elif(computer == 0 and you == 1):
    print("You Lose!")
elif(computer == 0 and you == 0):
    print("Its a draw")
elif(computer == -1 and you == -1):
    print("Its a draw")
elif(computer == 1 and you == 1):
    print("Its a draw")
else:
    print("Something went wrong!")



