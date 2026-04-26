# Name: Muteeba Jamin Mathew
# Registration Number: 25/BCC/BU/R/1002


import random

def play_game(round_number):
    print(f"\n--- Round {round_number} ---")

    # Increase difficulty each round (range grows)
    max_range = 100 + (round_number - 1) * 50
    number = random.randint(1, max_range)

    attempts = 0
    max_attempts = 7

    print(f"I have selected a number between 1 and {max_range}.")
    print(f"You have {max_attempts} attempts to guess it.")

    while attempts < max_attempts:
        user_input = input("Enter your guess: ")

        # Handle invalid input without losing attempt
        if not user_input.isdigit():
            print("Invalid input! Please enter a valid number.")
            continue

        guess = int(user_input)
        attempts += 1

        if guess < number:
            print("Too low")
        elif guess > number:
            print("Too high")
        else:
            print(f"Correct! You guessed the number in {attempts} attempts. Congratulations!")
            return  # End round if correct

    # If user fails after 7 attempts
    print(f"Game Over! The correct number was {number}.")


def main():
    round_number = 1

    while True:
        play_game(round_number)

        # Ask user if they want to play again
        choice = input("Do you want to play again? (yes/no): ").strip().lower()
        if choice != "yes":
            print("Thanks for playing!")
            break

        round_number += 1  # Increase difficulty next round


# Run the game
main()