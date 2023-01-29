import sys
import time
from colors import brown, green, grey, peach, pink, yellow
from learn import learn_about_months
from objects import Person, Player
from utils import clear, LINE, CENT, set_start_date
from validators import validate_menu_input, validate_name, validate_yes_no


def end_game():
    """
    Function to completely stop the app running.
    """
    time.sleep(0.25)
    print(green(LINE))
    time.sleep(0.25)
    print(green(CENT("Thanks for playing The Python Oregon Trail.")))
    time.sleep(0.25)
    print(green(CENT("Hopefully you didn't die of dysentery!")))
    time.sleep(0.25)
    print(green(LINE))
    time.sleep(1)
    sys.exit()


def ask_name(player, question):
    """
    Helper function to ask for player name, and all family names
    """
    while True:
        user_input = input(question)

        # validate if the user selected a valid option
        if validate_name(user_input):
            list_player_family(player)
            return user_input
        else:
            list_player_family(player)


def list_player_family(player):
    """
    Display the list of the wagon leader and family members.
    """
    clear()
    print(brown(LINE))
    print(peach(CENT("Your Wagon Party")))
    print(brown(LINE))
    print("")
    if player.name != "":
        print(f"\t{peach('1.')} {player.name} (you)")
    for i, person in enumerate(player.family):
        print(f"\t{peach(str(i+2)+'.')} {person.name}")
    print("")


def confirm_names(player):
    """
    Confirm if the list of names is correct.
    """
    while True:
        list_player_family(player)
        user_input = input("Are these names correct? ")

        # validate if the user selected a valid option
        if validate_yes_no(user_input):
            break

    if user_input[0].lower() == "n":
        # prompt for number to change
        while True:
            list_player_family(player)
            update_name = input(f"Change which name? {peach('[1-5]')} ")
            choices = ["1", "2", "3", "4", "5"]

            # validate 1-5
            if validate_menu_input(update_name, choices):
                break

        if update_name == "1":  # wagon leader
            player.name = ask_name(player, "What is the correct name of the wagon leader? ")  # noqa
        else:  # family members
            player.family[int(update_name) - 2].name = ask_name(player, f"What is the correct name for {peach(player.family[int(update_name) - 2].name)}? ")  # noqa
        confirm_names(player)


def pick_start_month():
    """
    Ask the user to pick their starting month from:
    March, April, May, June, or July
    """
    while True:
        clear()
        print(pink(LINE))
        print(pink(CENT("Pick your Departure Month")))
        print(pink(LINE))
        print("")
        print(CENT("It is 1848. Your jumping off place for Oregon"))
        print(CENT("is Independence, Missouri. You must decide which"))
        print(CENT("month to leave Independence.\n"))
        print(f'\t\t\t{pink("1. ")}{"March"}')
        print(f'\t\t\t{pink("2. ")}{"April"}')
        print(f'\t\t\t{pink("3. ")}{"May"}')
        print(f'\t\t\t{pink("4. ")}{"June"}')
        print(f'\t\t\t{pink("5. ")}{"July"}')
        print(f'\t\t\t{pink("6. ")}{"Ask for advice"}')

        user_input = input(f"\n\t\tWhat is your choice? {pink('[1-6]')} ")
        choices = ["1", "2", "3", "4", "5", "6"]

        # validate if the user selected a valid option
        if validate_menu_input(user_input, choices):
            # break

            if user_input == "1":
                month = 3
                break
            elif user_input == "2":
                month = 4
                break
            elif user_input == "3":
                month = 5
                break
            elif user_input == "4":
                month = 6
                break
            elif user_input == "5":
                month = 7
                break
            elif user_input == "6":
                learn_about_months()

    return set_start_date(month)


def start_game(profession):
    """
    Player begins defining their game data.
    """
    # initialize a new instance of the Player() with profession
    player = Player(profession)
    # set the starter cash based on profession
    player.profession_starter_cash()
    # ask for the player's name
    player.name = ""
    print(brown(LINE))
    print(peach(CENT("Your Wagon Party")))
    print(brown(LINE))
    print("\n")
    player.name = ask_name(player, "What is the first name of the wagon leader? ")  # noqa

    # build the player's family of 4 more persons
    for i in range(0, 4):
        list_player_family(player)
        family_member = Person(None)
        family_member.name = ask_name(player, "What is the first name of the next family member? ")  # noqa
        player.family.append(family_member)
    list_player_family(player)

    # confirm if names are correct
    confirm_names(player)

    # decide when to leave
    start_date = pick_start_month()
    print(start_date)

    # TODO: --------------------------------------------------------------------------------
    # TODO: next up: "Before leaving Independence, you should buy equipment and supplies..."
    # TODO: --------------------------------------------------------------------------------

    # print(f"Name: {player.name}\nProfession: {player.profession}\nCash: ${player.cash}")  # noqa
