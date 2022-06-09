# importing the module
import random

# functiomn that check for the winner


def winner_check(x, y):
    if x == "Scissors" and y == "Paper":
        print("\t HURRAY!, YOU WON!!")
    elif x == "Paper" and y == "Rock":
        print("\t HURRAY!, YOU WON!!")
    elif x == "Rock" and y == "Scissors":
        print("\t HURRAY!, YOU WON!!")
    elif y == "Scissors" and x == "Paper":
        print("\tYOU LOST!!")
    elif y == "Paper" and x == "Rock":
        print("\t YOU LOST!!")
    elif y == "Rock" and x == "Scissors":
        print("\tYOU LOST!!")


# welcoming the player
print("\tWelcome to the ROCK, PAPER AND SCISSORS GAME\n")

possibleOptions = ["Rock", "Paper", "Scissors"]
cpuMove = ""
playerMove = ""
while True:
    # defining the game
    print("Available moves are:")
    print("R for Rock")
    print("P for Paper")
    print("S for Scissors")
    cpuMove = random.choice(possibleOptions)
    playerMove = input("What's your move?: ")
    if playerMove.upper() == "R":
        playerMove = "Rock"
    elif playerMove.upper() == "P":
        playerMove = "Paper"
    elif playerMove.upper() == "S":
        playerMove = "Scissors"
    if playerMove not in possibleOptions:
        print("\tERROR! YOU ENTERED A WRONG INPUT")
        continue
    # printing out the moves
    print(f"Player({playerMove}) : CPU({cpuMove})")
    # checking for the winner using my function
    winner_check(playerMove, cpuMove)
    if playerMove == cpuMove:
        print("\tA tie, Start Over!\n")
        continue
    replay = input('Do you want to play agin: "Y" for YES "N" for NO? : ')
    if replay.upper() == "Y":
        continue
    else:
        break

# Closing game
print("\n\tTHANK YOU FOR PLAYING!")
