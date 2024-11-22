# Display art
from art import logo
from game_data import game_data
import random


# Functions
def format_data(account):
    """Format the account data into printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(user_guess, a_followers, b_followers):
    """Check if the user's guess is correct."""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"


# Main Game
print(logo)
score = 0
game_should_continue = True

# Start with two random accounts
account_b = random.choice(game_data)

while game_should_continue:
    # Make account_a the previous account_b
    account_a = account_b
    # Generate a new account_b, ensuring it's different from account_a
    account_b = random.choice(game_data)
    while account_a == account_b:
        account_b = random.choice(game_data)

    # Display the accounts
    print(f"Compare A: {format_data(account_a)}.")
    print(f"Compare B: {format_data(account_b)}.")

    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Get follower counts
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    # Check the user's guess
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Provide feedback
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        again = input("Would you like to play again? Type 'Y' or 'N': ").lower()
        if again == 'n':
            game_should_continue = False
        else:
            score = 0
            account_b = random.choice(game_data)  # Reset account_b for a new game
