# If player and computer choose the same decision then display ("Game Tied"),


# If the player chooses "Rock" and the computer chooses "Paper" display ("You lose"),
# If the player chooses "Scissors" and the computer chooses "Rock" display ("You Lose")  and
# If the player chooses "Paper" and the computer chooses "Scissors" then display ("You lose")
# -- Vice versa for other decisions.

# Continue to ask the player for their input until they say "I quit", at which time the game will then end and display ("Thank you for playing").


print("Hello, and welcome to COMPUTERIZED ROCK-PAPER-SCISSORS v1.0")

from random import randint

while True:
    # Ask the player to select a move and store it.
    player_choice = input(
        "Choose 'rock', 'paper', 'scissors', or type 'quit'. ").lower()
    cpu_choice = ""
    
    
    #If player chooses to quit, the game will end and display ("Thank you for playing").
         
    #Computer chooses an option after the player and store it. 
    
    #Both selections will be compared.
   
    #If selections are the same, print it's a tie.


    # If player chooses to quit, the game will end and display ("Thank you for playing").
    if player_choice == "quit":
        print("Thank you for playing")
        break


    # Computer chooses an option and store it.
    random_number = randint(1, 3)
    if random_number == 1:
        cpu_choice = "rock"
    elif random_number == 2:
        cpu_choice = "scissors"
    elif random_number == 3:
        cpu_choice = "paper"
    # Both selections will be compared.
    # If selections are the same, print it's a tie.
    if player_choice == cpu_choice:
        print("It's a tie, you suck!")
    # If player chooses rock and computer chooses scissors, the player wins.
    elif player_choice == "rock" and cpu_choice == "scissors":
        print(
            f"You chose {player_choice.title()} and the computer chose {cpu_choice.title()}. You win!")
    # If player chooses rock and computer chooses paper, the player loses the game.
    elif player_choice == "rock" and cpu_choice == "paper":
        print(
            f"You chose {player_choice.title()} and the computer chose {cpu_choice.title()}. You lose sucka!")
    # If player chooses scissors and computer chooses paper, the player wins.
    elif player_choice == "scissors" and cpu_choice == "paper":
        print(
            f"You chose {player_choice.title()} and the computer chose {cpu_choice.title()}. You win!")
    # If player chooses scissors and computer chooses rock, the player loses.
    elif player_choice == "scissors" and cpu_choice == "rock":
        print(
            f"You chose {player_choice.title()} and the computer chose {cpu_choice.title()}. You lose sucka!")
    # If player chooses paper and computer chooses rock, the player wins.
    elif player_choice == "paper" and cpu_choice == "rock":
        print(
            f"You chose {player_choice.title()} and the computer chose {cpu_choice.title()}. You win!")
    # If player chooses paper and computer chooses scissors, the player loses.
    elif player_choice == "paper" and cpu_choice == "scissors":
        print(
            f"You chose {player_choice.title()} and the computer chose {cpu_choice.title()}. You lose sucka!")
