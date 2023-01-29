import time
from colors import brown, gold, green, peach, red
from credits import credits
from learn import learn_about_trail
from utils import clear, CENT, LINE, ot_title, end_game
from validators import validate_menu_input


def leaderboard_menu():
    while True:
        clear()
        print(gold(LINE))
        print(gold(CENT("The Oregon Top Ten")))
        print(gold(LINE))

        print("\n\tYou may:\n")
        print("\t\t1. See the current Top Ten list")
        print("\t\t2. See the original Top Ten list")
        print("\t\t3. Return to the main menu")

        user_input = input("\n\tWhat is your choice? ")
        choices = ["1", "2", "3"]

        # validate if the user selected a valid option
        if validate_menu_input(user_input, choices):
            break

    clear()
    if user_input == "1":
        print(gold("... retrieving top 10 players list ..."))
        time.sleep(2)
        clear()
        print("TBD: Top 10 Players")
        time.sleep(2)
    elif user_input == "2":
        print(gold("... retrieving top 10 original overlanders ..."))
        time.sleep(2)
        clear()
        print("TBD: Top 10 original overlanders")
        time.sleep(2)


def main_menu():
    while True:
        clear()
        ot_title()

        print("\n\tYou may:\n")
        print("\t\t1. Travel the trail")
        print("\t\t2. Learn about the trail")
        print("\t\t3. See the Oregon Top Ten")
        print("\t\t4. Credits")
        print("\t\t5. End")

        # ------------------------------------
        # testing f-string alignment
        # https://stackoverflow.com/a/67540888
        # https://docs.python.org/3/library/string.html#format-specification-mini-language
        # ------------------------------------
        # print("\n")
        # a = "123456789 123456789 123456789 "
        # print(f'\t{"1234567890 ":.<40} {red(500)}')
        # print(f'\t{"12345678901234567890 ":.<40} {red(50)}')
        # print(f'\t{a:.<40} {red(555)}')
        # print("\n")
        # ------------------------------------

        user_input = input("\n\tWhat is your choice? ")
        choices = ["1", "2", "3", "4", "5"]

        # validate if the user selected a valid option
        if validate_menu_input(user_input, choices):
            break

    clear()
    if user_input == "1":
        print("1 selected")
    elif user_input == "2":
        learn_about_trail()
        main_menu()
    elif user_input == "3":
        leaderboard_menu()
        main_menu()
    elif user_input == "4":
        credits()
        main_menu()
    elif user_input == "5":
        end_game()
