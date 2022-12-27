import random
# The user's choice
def user():
    usere = input(""" (R)ock , (P)aper, (S)cissor: """)
    return usere
#The computer's random choice
def comp():
    computer = random.choice(["R", "P","S"])
    return computer
# A function to check answers
def checker(usere, computer):
    
    if usere == computer:
        print("Tie")
    else:
        if usere == "R" and computer == "S" or usere == "P" and computer == "R" or usere == "S" and computer =="P":
            print("You win")
        elif usere == "S" and computer == "R" or usere == "R" and computer == "P" or usere == "P" and computer =="S":
            print("You Lose")
        
#main function
def main():
    again = "y"
    while again == "y":
        usere = user()
        computer = comp()
        checker(usere,computer)
        
main()
