import random
from bcolors import bcolors as bcols

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

if __name__ == "__main__":
    """Main function."""
    play_game = True
    while play_game == True:
        while True:
            try:
                user_choice = int(input("\nWhat do you choose? Rock ('0'), Paper ('1') or Scissors ('2'): "))
                if user_choice in [0,1,2]:
                    break
            except ValueError as ve:
                print(ve)
                continue
            else:
                print(f"{bcols.FAIL}Input either 0, 1 or 2 please.{bcols.ENDC}")
                continue
            
        print(game_images[user_choice])
            
        computer_choice = random.randint(0, 2)
        print("Computer chose:")
        print(game_images[computer_choice])

        if user_choice == 0 and computer_choice == 2:
            print(f"{bcols.OKGREEN}You win!{bcols.ENDC}")
        elif computer_choice == 0 and user_choice == 2:
            print(f"{bcols.FAIL}You lose.{bcols.ENDC}")
        elif computer_choice > user_choice:
            print(f"{bcols.FAIL}You lose.{bcols.ENDC}")
        elif user_choice > computer_choice:
            print(f"{bcols.OKGREEN}You win!{bcols.ENDC}")
        elif computer_choice == user_choice:
            print(f"{bcols.WARNING}It's a draw.{bcols.ENDC}")

        while True:
            try:
                play_again = input("\nPlay again, 'yes' ('y') or 'no' ('n')? ").lower()
                if play_again == "no" or play_again == "n":
                    play_game = False    
                    break
                elif play_again == "yes" or play_again == "y":
                    break
            except Exception as e:
                print(e)
                continue
            else:
                print(f"{bcols.FAIL}Please input 'yes' or 'no'{bcols.ENDC}")
                continue
