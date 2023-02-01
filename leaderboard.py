import time
from colors import gold
from utils import clear, generate_title
from validators import validate_choice


def leaderboard_menu():
    """
    Creates a menu for players to check the leaderboards.
    """
    while True:
        generate_title(gold, "The Oregon Top Ten")

        print("\tYou may:\n")
        print(f'\t\t{gold("1. ")}{"See the current Top Ten list"}')
        print(f'\t\t{gold("2. ")}{"See the original Top Ten list"}')
        print(f'\t\t{gold("3. ")}{"Return to the main menu"}')

        user_input = input(f"\n\t\tWhat is your choice? {gold('[1-3]')} ")
        choices = ["1", "2", "3"]

        # validate if the user selected a valid option
        if validate_choice(user_input, choices):
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
