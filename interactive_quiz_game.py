"""
Interactive Quiz Game

This module implements an interactive quiz game where users can test their knowledge
across various topics. The game presents multiple-choice questions, tracks scores,
and provides feedback on performance.

Features:
- User-friendly interface with clear instructions
- Hidden answer input for fair gameplay
- Score tracking and percentage calculation
- Immediate feedback for each answer
- Final performance evaluation

Dependencies:
- getpass: For hiding user input during answer submission

Author: [Prerak Pithadiya]
Version: 1.0.0
Date: [18 Nov 2024]
"""

import getpass


def greet_user():
    """
    Display a welcome message to the user.

    This function prints a formatted welcome message and decorative separator
    to create an engaging start to the quiz game.
    """
    print("Welcome to the Ultimate Quiz Challenge!")
    print("Test your knowledge and see how much you know!")
    print("-" * 40)


def prompt_to_play():
    """
    Prompt the user to decide whether to play the quiz.

    Returns:
        bool: True if user wants to play, False if user declines.

    The function continuously prompts until a valid input (yes/no) is received,
    handling invalid inputs gracefully.
    """
    while True:
        user_response = (
            input("Would you like to participate in the quiz? (yes/no): ")
            .strip()
            .lower()
        )
        if user_response == "yes":
            print("\nFantastic! Let's get started!\n")
            return True
        elif user_response == "no":
            print("\nThank you! Maybe next time. Goodbye!")
            return False
        else:
            print("Invalid input. Please type 'yes' or 'no'.")


def ask_question(question, correct_answer):
    """
    Ask a single quiz question and evaluate the user's answer.

    Args:
        question (str): The quiz question to display.
        correct_answer (str): The correct answer to the question.

    Returns:
        bool: True if the user answered correctly, False otherwise.

    The function uses getpass to hide the user's input for fair gameplay and
    provides immediate feedback on the answer's correctness.
    """
    print("\n" + question)
    try:
        # Use getpass to hide the user's input
        user_answer = getpass.getpass("Your answer: ").strip().lower()
    except Exception as e:
        print(f"Error receiving input: {e}")
        return False

    if user_answer == correct_answer.lower():
        print("Correct!")
        return True
    else:
        print(f"Incorrect. The correct answer was '{correct_answer}'.")
        return False


def calculate_percentage(correct_answers, total_questions):
    """
    Calculate the percentage of correct answers.

    Args:
        correct_answers (int): Number of questions answered correctly.
        total_questions (int): Total number of questions in the quiz.

    Returns:
        float: Percentage of correct answers (0-100).

    This function converts the raw score into a percentage for easier
    interpretation of performance.
    """
    return (correct_answers / total_questions) * 100


def main():
    """
    Main function to run the quiz game.

    This function orchestrates the entire quiz game flow:
    1. Displays welcome message
    2. Prompts user to play
    3. Presents questions sequentially
    4. Tracks and calculates score
    5. Provides final performance feedback

    The quiz covers various topics including geography, science, history,
    and literature. A passing score is 70% or higher.
    """
    greet_user()

    if not prompt_to_play():
        return  # Exit the game if the user doesn't want to play.

    # Define quiz questions and answers
    questions = [
        ("What is the capital of France?", "Paris"),
        (
            "Which programming language is known as the 'language of the web'?",
            "JavaScript",
        ),
        ("What is the largest planet in our solar system?", "Jupiter"),
        ("What year did the Titanic sink?", "1912"),
        ("What is the chemical symbol for water?", "H2O"),
        ("Who wrote 'To Kill a Mockingbird'?", "Harper Lee"),
        ("Which continent is the Sahara Desert located on?", "Africa"),
        ("What is the smallest prime number?", "2"),
        ("What is the name of the process plants use to make food?", "Photosynthesis"),
        ("Which animal is known as the 'King of the Jungle'?", "Lion"),
    ]

    correct_answers = 0

    # Loop through each question
    for i, (question, answer) in enumerate(questions, start=1):
        print(f"\nQuestion {i}:")
        if ask_question(question, answer):
            correct_answers += 1

    # Calculate and display the results
    print("\nQuiz Complete!")
    print("-" * 40)
    print(
        f"You answered {correct_answers} out of {len(questions)} questions correctly."
    )
    percentage = calculate_percentage(correct_answers, len(questions))
    print(f"Your score: {percentage:.2f}%")
    if percentage >= 70:
        print("Great job! You passed the quiz!")
    else:
        print("Better luck next time!")


if __name__ == "__main__":
    main()
