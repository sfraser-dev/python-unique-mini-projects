import yu0005_ceasar_cipher_art
from bcolors import bcolors as bcols

def caesar(start_text: str, shift_amount: int, cipher_direction: str) -> None:
    """Encoding and decoding Caesar Cipher function."""
    end_text = ""
    if cipher_direction == "decode" or cipher_direction == "d":
        shift_amount *= -1
    for char in start_text:
        position = alphabet.index(char)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    if cipher_direction == "decode" or cipher_direction == "d":
        print(f"\nHere's the decoded result: {bcols.OKCYAN}{end_text}{bcols.ENDC}")
    else:
        print(f"\nHere's the encoded result: {bcols.OKCYAN}{end_text}{bcols.ENDC}")

if __name__ == "__main__":
    """Main function."""
    keep_ciphering = True
    while keep_ciphering:

        number_of_alphabets = 2
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        # repeat the alphabet 
        for _ in range(0,number_of_alphabets-1):
            alphabet += alphabet

        # Print the logo from art.py when the program starts.
        print(yu0005_ceasar_cipher_art.logo)

        while True:
            try:
                direction = input("\nType 'encode' ('e') to encode, type 'decode' ('d') to decrypt: ").lower()
                if direction in ["encode", "e", "decode", "d"] and type(direction)==str:
                    break
            except Exception as e:
                print(e)
                continue
            else:
                print(f"{bcols.FAIL}Please input 'encode', 'e', 'decode' or 'd'.{bcols.ENDC}\n")
                continue

        acceptable_text = True
        while True:
            try:
                text = input("\nType your message: ").lower()
                for i in text:
                    if i not in alphabet:   # only accept letters/text from the alphabet
                        acceptable_text = False
                        break   # break for loop
                else:   # for/else, executed if not broken out of for loop above
                    break   # break while loop
            except Exception as e:
                print(e)
                continue
            else:
                print(f"{bcols.FAIL}Text must consist of alphabetical characters only{bcols.ENDC}")
                acceptable_text = True
                continue

        while True:
            try:
                shift = int(input("\nType the shift number: "))
                if shift >=  1 and shift <= 25 and type(shift)==int:
                    break
            except ValueError as ve:
                print(ve)
                continue
            else:
                print(f"{bcols.FAIL}Please input an integer in range 1 to 25 inclusive.{bcols.ENDC}")
                continue

        caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

        while True:
            try:
                run_again = input("\nWould you like to cipher again, 'yes' ('y') or 'no' ('n')? ").lower()
                if run_again == "no" or run_again == "n":
                    keep_ciphering = False
                    break
                elif run_again == "yes" or run_again == "y":
                    break
            except Exception as e:
                print(e)
                continue
            else:
                print(f"{bcols.FAIL}Please enter 'yes' ('y') or 'no' ('n'){bcols.ENDC}")
                continue