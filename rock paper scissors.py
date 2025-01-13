#Rock Paper Scissors
#Stephy

#Init
import random

#Functions
def rpsgames():
    playerwins = 0 #Tracks players' wins
    computerwins = 0 #Tracks computer's wins
    ties = 0 #Tracks the ties between both the player and computer
    while True:
        #Step 1: Obtain the player's move
        print("Welcome to Rock, Paper, Scissors")
        print("What is your move?")
        player = input("Rock, Paper, Scissors, Go: ") #String
        player = player.lower()
        print("Your move is " + str(player) + "!")


        #Step 2: Generate the computer's move
        computer = random.randint(1, 3) #This function can generate random number
        if computer == 1:
            computer = "rock"
            print("The computer's move is Rock!")

        if computer == 2:
            computer = "paper"
            print("The computer's move is Paper!")

        if computer == 3:
            computer = "scissors"
            print("The computer's move is Scissors!")

        if player == "quit":
            print("Thank you for playing!")
            break #Loop ends after player "quits"

        #Step 3: The outcome

        if player == computer:
            print("It's a tie!")
            ties = ties + 1

        elif player == "rock" and computer == "paper":
            print("Computer wins!")
            computerwins = computerwins + 1 #Adds a point to computer

        elif player == "rock" and computer == "scissors":
            print("You win!")
            playerwins = playerwins + 1 #Adds a point to player

        elif player == "paper" and computer == "scissors":
            print("Computer wins!")
            computerwins = computerwins + 1

        elif player == "paper" and computer == "rock":
            print("You win!")
            playerwins = playerwins + 1

        elif player == "scissors" and computer == "paper":
            print("You win!")
            playerwins = playerwins + 1

        elif player == "scissors" and computer == "rock":
            print("Computer wins!")
            computerwins = computerwins + 1


        print("Player wins: " + str(playerwins)) #States player wins after each round
        print("Computer wins: " + str(computerwins)) #States computer wins after each round
        print("Ties: " + str(ties)) #States the ties after each round
#Main
rpsgames()
