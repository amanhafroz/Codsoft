import random

computer = random.choice([-1,0,1])
youstr = input("Enter your choice ( r for Rock, p for paper, s for scissors): ")
youDict = {"r":-1, "p":0, "s":1}
reverseDict = {-1:"Rock", 0:"Paper", 1:"Scissors"}

if youstr not in youDict:
    print("Invalid input. Please enter r,p or s")
else:
    you = youDict[youstr]
    print(f"you chose {reverseDict[you]}\n Computer chose {reverseDict[computer]}")
 
    if (computer == you):
        print("its a Draw")

    else:
        if(computer == -1 and you == 0):
            print("You win")

        elif(computer == -1 and you == 1):
            print("You lose")

        elif(computer == 0 and you == -1):
            print("You lose")

        elif(computer == 0 and you == 1):
            print("You win")

        elif(computer == 1 and you == -1):
            print("You win")

        elif(computer == 1 and you ==0 ):
            print("You lose")


print("Do you want to play one more round")
