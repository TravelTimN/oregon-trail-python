import time
from art import welcome_art
from colors import orange
from credits import credits
from game import end_game
from independence import pick_profession, konami
from leaderboard import leaderboard_menu
from learn import learn_about_trail
from utils import clear, generate_title
from validators import validate_choice


def main_menu():
    """
    Starts the main game play menu.
    """
    while True:
        generate_title(orange, "The Python Oregon Trail")

        print("\tYou may:\n")
        time.sleep(0.05)
        print(f'\t\t{orange("1. ")}{"Travel the trail"}')
        time.sleep(0.05)
        print(f'\t\t{orange("2. ")}{"Learn about the trail"}')
        time.sleep(0.05)
        print(f'\t\t{orange("3. ")}{"See the Oregon Top Ten"}')
        time.sleep(0.05)
        print(f'\t\t{orange("4. ")}{"Credits"}')
        time.sleep(0.05)
        print(f'\t\t{orange("5. ")}{"End"}')
        time.sleep(0.05)

        user_input = input(f"\n\t\tWhat is your choice? {orange('[1-5]')} ")
        choices = ["1", "2", "3", "4", "5", "uuddlrlrba"]

        # validate if the user selected a valid option
        if validate_choice(user_input, choices):

            clear()
            if user_input == "1":  # starts the game
                pick_profession()
                break  # TODO: stops at end: need cycle to reset first!!
            elif user_input == "2":  # learn about the trail
                learn_about_trail()
            elif user_input == "3":  # check the leaderboard
                leaderboard_menu()
            elif user_input == "4":  # see credits
                credits()
            elif user_input == "5":  # ends the game
                end_game()
            elif user_input == "uuddlrlrba":  # konami easter egg for testing
                konami()


if __name__ == "__main__":
    clear()
    welcome_art()
    main_menu()

    # for name in dir():
    #     if not name.startswith("_"):
    #         del globals()[name]
