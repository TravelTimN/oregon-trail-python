import time
import sys
from utils import clear, CENT, LINE
from colors import peach, red, green, brown
from validators import validate_user_input


def main_menu():
    while True:
        # clear()
        print(brown(LINE))
        print(peach(CENT("The Oregon Trail")))
        print(brown(LINE))

        print("You may:\n")
        print("\t1. Travel the trail")
        print("\t2. Learn about the trail")
        print("\t3. See the Oregon Top Ten")
        print("\t4. End")

        user_input = input("\nWhat is your choice? ")
        choices = ["1", "2", "3", "4"]

        # validate if the user selected a valid option
        if validate_user_input(user_input, choices):
            break

    clear()
    if user_input == "1":
        # instructions()
        print("1 selected")
    elif user_input == "2":
        # start_game()
        print("2 selected")
    elif user_input == "3":
        # exit_game()
        print("3 selected")
    elif user_input == "4":
        print(
            green(LINE) + "\n" +
            green(CENT("Thanks for playing The Oregon Trail (Python)!")) +
            "\n" + green(LINE) + "\n"
        )
        sys.exit()
