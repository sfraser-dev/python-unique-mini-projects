import random
from bcolors import bcolors as bcols

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

if __name__ == "__main__":
    """Main function."""
    print("Welcome to the Password Generator!")
    keep_generating = True
    while keep_generating == True:

        while True:
            try:
                nr_letters= int(input("\nHow many letters would you like in your password? ")) 
                if type(nr_letters) == int:
                    break
            except ValueError as ve:
                print(ve)
                continue
            else:
                print(f"{bcols.FAIL}Please input an integer.{bcols.ENDC}")
                continue

        while True:
            try:
                nr_numbers = int(input("\nHow many numbers would you like? "))
                if type(nr_numbers)== int:
                    break
            except ValueError as ve:
                print(ve)
                print(f"{bcols.FAIL}Please input an integer.{bcols.ENDC}")
                continue
            else:
                print(f"{bcols.FAIL}Please input an integer.{bcols.ENDC}")
                continue

        while True:
            try:
                nr_symbols = int(input("\nHow many symbols would you like? "))
                if type(nr_symbols) == int:
                    break
            except ValueError as ve:
                print(ve)
                continue
            else:
                print(f"{bcols.FAIL}Please input an integer.{bcols.ENDC}")
                continue

        new_pass = []
        for x in range(0,nr_letters):
            new_pass.append(letters[random.randint(0,len(letters)-1)])
        for x in range(0,nr_numbers):
            new_pass.append(numbers[random.randint(0,len(numbers)-1)])
        for x in range(0,nr_symbols):
            new_pass.append(symbols[random.randint(0,len(symbols)-1)])

        # Order of characters randomised
        random.shuffle(new_pass)

        # Print unpacked list elements
        print("\nThe newly generated password is: ",end="")
        for x in range(len(new_pass)):
            print(f"{bcols.OKCYAN}{new_pass[x]}{bcols.ENDC}",end="")
        print() 

        while True:
            try:
                user_input = input("\nGenerate another password, 'yes' ('y') or 'no' ('n')? ")
                if user_input == "no" or user_input == "n":
                    keep_generating = False
                    break
                elif user_input == "yes" or user_input == "y":
                    break
            except Exception as e:
                print(e)
                continue
            else: 
                print(f"{bcols.FAIL}Please input 'yes' or 'no'{bcols.ENDC}")
                continue
