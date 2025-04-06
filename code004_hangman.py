import random
from code004_hangman_words import word_list
from bcolors import bcolors as bcols
from code004_hangman_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

if __name__ == "__main__":
    """Main function."""
    play_again = True
    while play_again == True:
        # choose a word
        chosen_word = random.choice(word_list)
        word_length = len(chosen_word)

        # game setup
        end_of_game = False
        lives = 6

        # Import the logo from hangman_art.py and print it at the start of the game.
        print(logo)

        # Create blanks in "display" list
        display = []
        for _ in range(word_length):
            display += "_"

        wrong_letters = []
        # Game loop
        while not end_of_game:
            while True:
                try:
                    guess = input("\nGuess a letter: ").lower()
                    if type(guess) == str and len(guess) == 1 and guess in alphabet:
                        break
                except Exception as e:
                    print(e)
                    continue
                else:
                    print(f"{bcols.FAIL}Please input a single letter from the alphabet{bcols.ENDC}.")
                    continue

            # If the user has entered a letter they've already guessed, print the letter and let them know.
            if guess in display:
                print(f"You've already guessed {guess} correctly")

            # Check guessed letter
            for position in range(word_length):
                letter = chosen_word[position]
                if letter == guess:
                    display[position] = letter

            # Check if user is wrong.
            if guess in wrong_letters:
                print(f"We know '{guess}' isn't in the word already... continuing")
            elif guess not in chosen_word:
                # If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
                print(f"You guessed {guess}, that's not in the word. You lose a life.")
                wrong_letters += guess
                
                lives -= 1
                if lives == 0:
                    end_of_game = True
                    print(f"\n{bcols.OKCYAN}The answer was: {chosen_word}{bcols.ENDC}")
                    print(f"\n{bcols.FAIL}You lose.{bcols.ENDC}")

            # Join all the elements in the list and turn it into a String.
            print(f"\n{bcols.OKBLUE}{' '.join(display)}{bcols.ENDC}")
            # Show previous wrongly guess letters
            print("\nWrongly guessed letters:",end=" ")
            for x in range(len(wrong_letters)):
                print(f"{bcols.WARNING}{wrong_letters[x]}{bcols.ENDC}",end=" ")
            print()

            # Check if user has got all letters.
            if "_" not in display:
                end_of_game = True
                print(f"\n{bcols.OKGREEN}You win.{bcols.ENDC}")

            # Import the stages from hangman_art.py.
            from code004_hangman_art import stages
            print(stages[lives])

        while True:
            try:
                user_input = input("\nWould you like to play again, 'yes' ('y') or 'no' ('n')? ").lower()
                if user_input == "no" or user_input == "n":
                    play_again = False
                    break
                elif user_input == "yes" or user_input == "y":
                    end_of_game = False 
                    break
            except Exception as e:
                print(e)
                continue
            else:
                print(f"{bcols.FAIL}Please enter 'yes' ('y') or 'no' ('n'){bcols.ENDC}")
                continue