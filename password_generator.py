"""
Password Generator

This module provides functionality to generate secure passwords based on user preferences.
It allows users to specify the password length and whether to include digits and special characters.

The module includes a colorful command-line interface with emoji support for better user experience.

Classes:
    Colors: Contains ANSI escape codes for terminal text coloring

Functions:
    generate_password: Generates a password based on specified criteria
    get_yes_no_input: Handles yes/no user input with validation
    main: Main program loop for the password generator

Author: Prerak Pithadiya
Version: 1.0
"""

import random
import string


class Colors:
    """
    ANSI escape codes for terminal text coloring.

    Attributes:
        HEADER (str): Purple text
        OKBLUE (str): Blue text
        OKGREEN (str): Green text
        WARNING (str): Yellow text
        FAIL (str): Red text
        ENDC (str): Reset text formatting
        BOLD (str): Bold text
        UNDERLINE (str): Underlined text
    """

    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def generate_password(length, include_digits, include_special_chars):
    """
    Generates a password based on user preferences.

    The function creates a password using a combination of ASCII letters, digits,
    and special characters based on the user's specifications. It ensures the
    password meets the minimum length requirement.

    Args:
        length (int): The desired length of the password
        include_digits (bool): Whether to include digits (0-9) in the password
        include_special_chars (bool): Whether to include special characters in the password

    Returns:
        str: The generated password, or an error message if length is invalid

    Example:
        >>> generate_password(8, True, True)
        'K9#mP2*q'
    """
    # Start with letters
    characters = string.ascii_letters  # Contains both lowercase and uppercase letters

    # Add digits if requested
    if include_digits:
        characters += string.digits

    # Add special characters if requested
    if include_special_chars:
        characters += string.punctuation

    # Ensure the password is at least of the requested length
    if length < 1:
        return "Password length must be at least 1."

    # Generate password
    password = "".join(random.choice(characters) for _ in range(length))
    return password


def get_yes_no_input(prompt):
    """
    Get a yes or no input from the user with validation.

    Continuously prompts the user until a valid yes/no response is received.
    Accepts 'yes', 'y', 'no', 'n' in any case as valid inputs.

    Args:
        prompt (str): The prompt to display to the user

    Returns:
        bool: True for 'yes'/'y', False for 'no'/'n'

    Example:
        >>> get_yes_no_input("Continue? (yes/no): ")
        Continue? (yes/no): yes
        True
    """
    while True:
        response = input(prompt).strip().lower()
        if response in ["yes", "y"]:
            return True
        elif response in ["no", "n"]:
            return False
        else:
            print(
                f"{Colors.FAIL}❌ Invalid input. Please enter 'yes' or 'no'. 🚫{Colors.ENDC}"
            )


def main():
    """
    Main function to run the password generator.

    Provides an interactive command-line interface for the password generator.
    Features include:
    - Custom password length input
    - Option to include digits
    - Option to include special characters
    - Option to generate multiple passwords
    - Error handling for invalid inputs
    - Colorful interface with emoji feedback
    """
    print(
        f"{Colors.HEADER}{Colors.BOLD}🔐 Welcome to the Password Generator! 🛡️{Colors.ENDC}"
    )

    while True:
        try:
            # Get password length from user
            length = int(
                input(
                    f"{Colors.OKBLUE}📏 Enter the desired length of the password: {Colors.ENDC}"
                )
            )

            # Ask user if they want to include digits
            include_digits = get_yes_no_input(
                f"{Colors.OKBLUE}🔢 Include digits (0-9)? (yes/no): {Colors.ENDC}"
            )

            # Ask user if they want to include special characters
            include_special_chars = get_yes_no_input(
                f"{Colors.OKBLUE}⚡ Include special characters (e.g., !@#$%^&*)? (yes/no): {Colors.ENDC}"
            )

            # Generate the password
            password = generate_password(length, include_digits, include_special_chars)

            # Display the generated password
            print(
                f"\n{Colors.OKGREEN}✅ Your generated password is: {Colors.BOLD}{password} 🔑{Colors.ENDC}"
            )

            # Ask if the user wants to generate another password
            another = get_yes_no_input(
                f"\n{Colors.OKBLUE}🔄 Would you like to generate another password? (yes/no): {Colors.ENDC}"
            )
            if not another:
                print(
                    f"{Colors.WARNING}👋 Thank you for using the Password Generator! Goodbye! ✨{Colors.ENDC}"
                )
                break

        except ValueError:
            print(
                f"{Colors.FAIL}❌ Invalid input. Please enter a valid number for the password length. 🚫{Colors.ENDC}"
            )


if __name__ == "__main__":
    main()
