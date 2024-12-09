"""
LeetCode Statistics Analyzer

This module provides functionality to fetch and analyze a user's LeetCode problem-solving statistics.
It uses the LeetCode GraphQL API to retrieve data about solved problems across different difficulty levels.

Features:
- Fetch user statistics from LeetCode's GraphQL API
- Parse and validate API responses
- Display formatted statistics by difficulty level
- Error handling for API requests and data parsing

Dependencies:
- requests: For making HTTP requests to the LeetCode API
- json: For debugging and response inspection (if needed)

"""

import requests
import json
import argparse


def get_leetcode_stats(username):
    """
    Fetches and parses LeetCode user statistics using the GraphQL API.

    This function makes a POST request to LeetCode's GraphQL API to retrieve
    problem-solving statistics for a given username. It handles various error
    cases and validates the response data structure.

    Args:
        username (str): LeetCode username to fetch statistics for.

    Returns:
        dict: A dictionary containing problem counts by difficulty level with the following structure:
            {
                'Easy': int,
                'Medium': int,
                'Hard': int
            }
            Returns None if an error occurs during fetching or parsing.

    Raises:
        requests.exceptions.RequestException: If there's an error making the HTTP request
        KeyError: If the response doesn't contain the expected data structure
    """
    api_url = "https://leetcode.com/graphql"

    query = {
        "query": """
        query getUserProfile($username: String!) {
          matchedUser(username: $username) {
            submitStats {
              acSubmissionNum {
                difficulty
                count
              }
            }
          }
        }
        """,
        "variables": {"username": username},
    }

    try:
        response = requests.post(api_url, json=query)
        response.raise_for_status()

        # Parse JSON response
        data = response.json()
        print("\nDebug: Raw API Response:")
        print(json.dumps(data, indent=4))  # Debugging: Inspect API response
        # Validate structure
        if not data or "data" not in data or not data["data"].get("matchedUser"):
            print(
                "Error: Unable to fetch user data. The username might be incorrect or the API response is invalid."
            )
            return None

        ac_stats = data["data"]["matchedUser"]["submitStats"]["acSubmissionNum"]
        return {item["difficulty"]: item["count"] for item in ac_stats}

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching data: {e}")
        return None
    except KeyError:
        print("Error: Unable to parse user data. Ensure the username is correct.")
        return None


def display_stats(stats):
    """
    Displays the LeetCode statistics in a user-friendly format.

    This function takes the processed statistics dictionary and presents it
    in a readable format, showing the number of problems solved for each
    difficulty level.

    Args:
        stats (dict): User statistics dictionary containing counts by difficulty level.
            Expected format: {'Easy': int, 'Medium': int, 'Hard': int}

    Example output:
        LeetCode Problem-Solving Stats:
        Easy Problems Solved: 50
        Medium Problems Solved: 30
        Hard Problems Solved: 10
    """
    if stats:
        print("\nLeetCode Problem-Solving Stats:")
        print(f"Easy Problems Solved: {stats.get('Easy', 0)}")
        print(f"Medium Problems Solved: {stats.get('Medium', 0)}")
        print(f"Hard Problems Solved: {stats.get('Hard', 0)}")
    else:
        print("No statistics available to display.")


def main():
    """
    Main entry point for the LeetCode Statistics Analyzer.

    This function handles the user interaction flow:
    1. Displays a welcome message
    2. Prompts for the user's LeetCode username
    3. Fetches the statistics
    4. Displays the results

    The function can be run directly when the script is executed
    or called from another module.
    """
    print("Welcome to the LeetCode Stats Analyzer!")
    username = input("Enter your LeetCode username: ").strip()

    print("\nFetching your data, please wait...")
    stats = get_leetcode_stats(username)

    display_stats(stats)


if __name__ == "__main__":
    main()
