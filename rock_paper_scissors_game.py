"""
Rock, Paper, Scissors Game

This module implements a classic Rock, Paper, Scissors game where a user plays against
the computer. The game continues until the user chooses to quit, keeping track of the
scores throughout multiple rounds.

The game follows traditional rules:
- Rock crushes Scissors
- Scissors cut Paper
- Paper covers Rock

Functions:
    display_welcome_message(): Displays the initial game rules and instructions
    get_user_choice(): Gets and validates the user's choice
    get_computer_choice(): Generates the computer's random choice
    determine_winner(user_choice, computer_choice): Determines the winner of a round
    display_round_result(user_choice, computer_choice, winner): Shows the result of each round
    main(): Controls the main game loop and scoring
"""

import random


def display_welcome_message():
    """
    Display the welcome message and game rules to the user.
    This function prints the basic rules and valid input options.
    """
    print("Welcome to the Rock, Paper, Scissors Game!")
    print("Rules: Choose one of Rock, Paper, or Scissors.")
    print("The computer will also make a choice.")
    print("The winner is determined as follows:")
    print("- Rock crushes Scissors")
    print("- Scissors cut Paper")
    print("- Paper covers Rock")
    print("Enter 'Q' or 'q' to quit at any time.\n")


def get_user_choice():
    """
    Get and validate the user's choice input.

    Returns:
        str: The user's choice ('Rock', 'Paper', 'Scissors', or 'Quit')
    """
    while True:
        user_input = (
            input("Enter your choice (Rock, Paper, Scissors): ").strip().capitalize()
        )
        if user_input in ["Rock", "Paper", "Scissors"]:
            return user_input
        elif user_input.lower() == "q":
            return "Quit"
        else:
            print("Invalid choice. Please enter 'Rock', 'Paper', or 'Scissors'.\n")


def get_computer_choice():
    """
    Generate a random choice for the computer.

    Returns:
        str: The computer's choice ('Rock', 'Paper', or 'Scissors')
    """
    return random.choice(["Rock", "Paper", "Scissors"])


def determine_winner(user_choice, computer_choice):
    """
    Determine the winner of a round based on the choices made.

    Args:
        user_choice (str): The user's choice
        computer_choice (str): The computer's choice

    Returns:
        str: The result ('User', 'Computer', or 'Tie')
    """
    rules = {
        "Rock": "Scissors",  # Rock beats Scissors
        "Scissors": "Paper",  # Scissors beat Paper
        "Paper": "Rock",  # Paper beats Rock
    }
    if user_choice == computer_choice:
        return "Tie"
    elif rules[user_choice] == computer_choice:
        return "User"
    else:
        return "Computer"


def display_round_result(user_choice, computer_choice, winner):
    """
    Display the results of a single round.

    Args:
        user_choice (str): The user's choice
        computer_choice (str): The computer's choice
        winner (str): The winner of the round ('User', 'Computer', or 'Tie')
    """
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if winner == "Tie":
        print("It's a tie!")
    elif winner == "User":
        print("You win this round!")
    else:
        print("Computer wins this round!")


def main():
    """
    Main game loop that controls the flow of the game.

    This function:
    - Initializes the score counters
    - Manages the game rounds
    - Handles user input for continuing or quitting
    - Displays the final scores
    """
    user_wins = 0
    computer_wins = 0

    display_welcome_message()

    while True:
        user_choice = get_user_choice()
        if user_choice == "Quit":
            break

        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)

        if winner == "User":
            user_wins += 1
        elif winner == "Computer":
            computer_wins += 1

        display_round_result(user_choice, computer_choice, winner)

        print(f"\nScores -> You: {user_wins}, Computer: {computer_wins}")
        print("-" * 30)

        play_again = (
            input(
                "Do you want to play another round? (Press Enter to continue or 'Q' to quit): "
            )
            .strip()
            .lower()
        )
        if play_again == "q":
            break

    print("\nGame Over!")
    print(f"Final Scores -> You: {user_wins}, Computer: {computer_wins}")
    print("Thanks for playing! Goodbye!")


main()
