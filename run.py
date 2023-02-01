import time
# import pyfiglet
from colors import orange
from credits import credits
from independence import end_game, pick_profession
# from landmarks import landmarks
from leaderboard import leaderboard_menu
from learn import learn_about_trail
from utils import clear, generate_title
from validators import validate_choice


# f = pyfiglet.FigletFont.getFonts()
# for a in f[:10]:
#     print(a)
#     print(pyfiglet.figlet_format("The Oregon Trail", font=a))


def main_menu():
    """
    Starts the main game play menu.
    """
    while True:
        clear()
        generate_title(orange, "The Python Oregon Trail")

        print("\tYou may:\n")
        print(f'\t\t{orange("1. ")}{"Travel the trail"}')
        print(f'\t\t{orange("2. ")}{"Learn about the trail"}')
        print(f'\t\t{orange("3. ")}{"See the Oregon Top Ten"}')
        print(f'\t\t{orange("4. ")}{"Credits"}')
        print(f'\t\t{orange("5. ")}{"End"}')

        # ------------------------------------
        # testing f-string alignment
        # https://stackoverflow.com/a/67540888
        # https://docs.python.org/3/library/string.html#format-specification-mini-language
        # ------------------------------------
        # print("\n")
        # a = "123456789 123456789 123456789 "
        # print(f'\t{"1234567890 ":.<40} {orange(500)}')
        # print(f'\t{"12345678901234567890 ":.<40} {orange(50)}')
        # print(f'\t{a:.<40} {orange(555)}')
        # print("\n")
        # ------------------------------------

        user_input = input(f"\n\t\tWhat is your choice? {orange('[1-5]')} ")
        choices = ["1", "2", "3", "4", "5"]

        # validate if the user selected a valid option
        if validate_choice(user_input, choices):
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


if __name__ == "__main__":
    clear()

    # for landmark in landmarks:
    #     for conversation in landmark["conversations"]:
    #         if conversation["speech"] != "":
    #             print(conversation["speech"])
    #             print("")
    # input("")

    # for name in dir():
    #     if not name.startswith("_"):
    #         del globals()[name]

    main_menu()
