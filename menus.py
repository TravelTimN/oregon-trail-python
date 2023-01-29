import time
from colors import brown, gold, red, pink
from credits import credits
from game import start_game, end_game
from learn import learn_about_trail, learn_about_professions
from utils import clear, CENT, LINE, ot_title
from validators import validate_menu_input


def pick_profession():
    """
    Creates a menu for player to pick their profession.
    """
    while True:
        clear()
        print(pink(LINE))
        print(pink(CENT("Pick your Profession")))
        print(pink(LINE))

        print("\n\tMany kinds of people made the trip to Oregon.")
        print("\n\tYou may:\n")
        print(f'\t\t{pink("1. ")}{"Be a banker from Boston"}')
        print(f'\t\t{pink("2. ")}{"Be a carpenter from Ohio"}')
        print(f'\t\t{pink("3. ")}{"Be a farmer from Illinois"}')
        print(f'\t\t{pink("4. ")}{"Find out the differences between these choices"}')  # noqa

        user_input = input("\n\tWhat is your choice? ")
        choices = ["1", "2", "3", "4"]

        # validate if the user selected a valid option
        if validate_menu_input(user_input, choices):
            break

    clear()
    # start the game with the user's selected profession
    if user_input == "1":
        start_game("banker")
    elif user_input == "2":
        start_game("carpenter")
    elif user_input == "3":
        start_game("farmer")
    elif user_input == "4":
        learn_about_professions()
        pick_profession()


def leaderboard_menu():
    """
    Creates a menu for players to check the leaderboards.
    """
    while True:
        clear()
        print(gold(LINE))
        print(gold(CENT("The Oregon Top Ten")))
        print(gold(LINE))

        print("\n\tYou may:\n")
        print(f'\t\t{gold("1. ")}{"See the current Top Ten list"}')
        print(f'\t\t{gold("2. ")}{"See the original Top Ten list"}')
        print(f'\t\t{gold("3. ")}{"Return to the main menu"}')

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
        print(f'\t\t{brown("1. ")}{"Travel the trail"}')
        print(f'\t\t{brown("2. ")}{"Learn about the trail"}')
        print(f'\t\t{brown("3. ")}{"See the Oregon Top Ten"}')
        print(f'\t\t{brown("4. ")}{"Credits"}')
        print(f'\t\t{brown("5. ")}{"End"}')

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
    if user_input == "1":  # starts the game
        pick_profession()
    elif user_input == "2":  # learn about the trail
        learn_about_trail()
        main_menu()
    elif user_input == "3":  # check the leaderboard
        leaderboard_menu()
        main_menu()
    elif user_input == "4":  # see credits
        credits()
        main_menu()
    elif user_input == "5":  # ends the game
        end_game()
