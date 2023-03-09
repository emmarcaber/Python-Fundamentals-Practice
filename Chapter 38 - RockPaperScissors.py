# CHAPTER 38
# RockPaperScissors Game

import random

while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper, scissors? ").lower()

    if player == computer:
        print(f"computer: {computer}")
        print(f"player: {player}")
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print(f"computer: {computer}")
            print(f"player: {player}")
            print("You lose!")
        elif computer == "scissors":
            print(f"computer: {computer}")
            print(f"player: {player}")
            print("You win!")
    elif player == "paper":
        if computer == "scissors":
            print(f"computer: {computer}")
            print(f"player: {player}")
            print("You lose!")
        elif computer == "rock":
            print(f"computer: {computer}")
            print(f"player: {player}")
            print("You win!")
    elif player == "scissors":
        if computer == "rock":
            print(f"computer: {computer}")
            print(f"player: {player}")
            print("You lose!")
        elif computer == "paper":
            print(f"computer: {computer}")
            print(f"player: {player}")
            print("You win!")

    play_again = input("Play again? (yes/no)? ").lower()

    if play_again != "yes":
        break

print("Bye!")
