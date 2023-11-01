#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

# write 'hello world' to the console


options = ["rock", "paper", "scissors"]
player_score = 0

def get_player_choice():
    while True:
        choice = input("Choose rock, paper, or scissors: ").lower()
        if choice in options:
            return choice
        else:
            print("Invalid option. Please choose again.")

def get_computer_choice():
    return random.choice(options)

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        return "player"
    else:
        return "computer"

def play_again():
    while True:
        choice = input("Do you want to play again? (y/n): ").lower()
        if choice == "y":
            return True
        elif choice == "n":
            return False
        else:
            print("Invalid option. Please choose again.")

def print_score():
    print("Your score: {}".format(player_score))

def play_game():
    global player_score
    while True:
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        print("You chose {}.".format(player_choice))
        print("The computer chose {}.".format(computer_choice))
        winner = determine_winner(player_choice, computer_choice)
        if winner == "tie":
            print("It's a tie!")
        elif winner == "player":
            print("You win!")
            player_score += 1
        else:
            print("You lose!")
        print_score()
        if not play_again():
            break

if __name__ == "__main__":
    play_game()