import os
import sys
from yu0007_calculator_art import logo
from bcolors import bcolors as bcols

def clear() -> None:
    """Cross-platform clear screen function"""
    os.system("cls" if os.name == "nt" else "clear")

def add(n1: float, n2: float) -> float:
    """Simple addition function."""
    return n1 + n2

def subtract(n1: float, n2: float) -> float:
    """Simple subtraction function."""
    return n1 - n2

def multiply(n1: float, n2: float) -> float:
    """Simple multiplication function."""
    return n1 * n2

def divide(n1: float, n2: float) -> float:
    """Simple division function."""
    return n1 / n2

# dictionary of mathematical operations
operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

def calculator():
    print(logo)

    while True:
        try:
            num1 = float(input("\nWhat's the first number?: "))
            if type(num1) == float:
                break
        except ValueError as ve:
            print(f"{bcols.FAIL}{ve}{bcols.ENDC}")
            continue
        else:
            print(f"{bcols.FAIL}Please input a number.{bcols.ENDC}")
            continue

    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        while True:
            try: 
                operation_symbol = input("\nPick an operation: ")
                if operation_symbol in ["+", "-", "/", "*"] and type(operation_symbol) == str:
                    break
            except Exception as e:
                print(e)
                continue
            else:
                print(f"{bcols.FAIL}Please specify '+', '-', '/' or '*'{bcols.ENDC}")
                continue
        while True:
            try:
                num2 = float(input("\nWhat's the next number?: "))
                if type(num2) == float:
                    break
            except ValueError as ve:
                print(f"{bcols.FAIL}{ve}{bcols.ENDC}")
                continue
            else:
                print(f"{bcols.FAIL}Please input a number.{bcols.ENDC}")
                continue

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        while True:
            try:
                user_input = input(f"\nType 'y' to continue calculating with {answer}, type 'n' to start a new calculation or type 'x' to exit: ").lower()
                if user_input == "y":
                    num1 = answer
                    break
                elif user_input == "n":
                    should_continue = False
                    clear()
                    # recursive calculator function 
                    calculator()
                    break
                elif user_input == "x":
                    sys.exit()
            except Exception as e:
                print(e)
                continue
            else:
                print(f"Please input 'y', 'n' or 'x'.")
                continue

if __name__ == """__main__""":
    """Main function."""
    calculator()
