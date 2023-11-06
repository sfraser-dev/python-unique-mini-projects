import random
import bcolors

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

play_game = True
while play_game == True:
    while True:
        try:
            user_choice = int(input("\nWhat do you choose? Rock ('0'), Paper ('1') or Scissors ('2'): "))
            if user_choice in [0,1,2]:
                break
        except Exception as e:
            print(e)
            continue
        else:
            print(f"{bcolors.bcolors.FAIL}Input either 0, 1 or 2 please.{bcolors.bcolors.ENDC}")
            continue
        
    print(game_images[user_choice])
        
    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print(f"{bcolors.bcolors.OKGREEN}You win!{bcolors.bcolors.ENDC}")
    elif computer_choice == 0 and user_choice == 2:
        print(f"{bcolors.bcolors.FAIL}You lose.{bcolors.bcolors.ENDC}")
    elif computer_choice > user_choice:
        print(f"{bcolors.bcolors.FAIL}You lose.{bcolors.bcolors.ENDC}")
    elif user_choice > computer_choice:
        print(f"{bcolors.bcolors.OKGREEN}You win!{bcolors.bcolors.ENDC}")
    elif computer_choice == user_choice:
        print(f"{bcolors.bcolors.WARNING}It's a draw.{bcolors.bcolors.ENDC}")

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
            print(f"{bcolors.bcolors.FAIL}Please input 'yes' or 'no'{bcolors.bcolors.ENDC}")
            continue
