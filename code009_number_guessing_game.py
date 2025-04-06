import random
from code009_number_guessing_game_art import logo

def choose_difficulty():
    while True:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if difficulty == 'easy':
            return 10
        elif difficulty == 'hard':
            return 5
        else:
            print("Invalid choice. Please type 'easy' or 'hard'.")

def guess_number():
    print(logo)
    print("Guess a number between 1 and 100.")

    target_number = random.randint(1, 100)
    attempts_remaining = choose_difficulty()

    while attempts_remaining > 0:
        print(f"\nYou have {attempts_remaining} attempts remaining to guess the number.")
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess == target_number:
            print(f"You got it! The answer was {target_number}.")
            return
        elif guess < target_number:
            print("Too low.")
        else:
            print("Too high.")

        attempts_remaining -= 1

    print(f"You're out of guesses. The number was {target_number}. Better luck next time!")

if __name__ == "__main__":
    guess_number()
