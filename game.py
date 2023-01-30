import sys
import time
from colors import aqua, brown, green, grey, peach, pink, red, yellow
from learn import learn_about_months
from objects import Game, Person, Player
from utils import clear, LINE, CENT
from validators import validate_menu_input, validate_name, validate_yes_no


PLAYER = GAME = None


def end_game():
    """
    Function to completely stop the app running.
    """
    time.sleep(0.25)
    print(red(LINE))
    time.sleep(0.25)
    print(red(CENT("Thanks for playing The Python Oregon Trail.")))
    time.sleep(0.25)
    print(red(CENT("Hopefully you didn't die of dysentery!")))
    time.sleep(0.25)
    print(red(LINE))
    time.sleep(1)
    sys.exit()


def ask_name(question):
    """
    Helper function to ask for player name, and all family names
    """
    while True:
        user_input = input(question)

        # validate if the user selected a valid option
        if validate_name(user_input):
            list_player_family()
            return user_input
        else:
            list_player_family()


def list_player_family():
    """
    Display the list of the wagon leader and family members.
    """
    global PLAYER

    clear()
    print(green(LINE))
    print(green(CENT("Your Wagon Party")))
    print(green(LINE))
    print("")
    if PLAYER.name != "":
        print(f"\t{aqua('1)')} {PLAYER.name} {aqua('[you]')}")
    for i, person in enumerate(PLAYER.family):
        print(f"\t{aqua(str(i+2)+')')} {person.name}")
    print("")


def confirm_names():
    """
    Confirm if the list of names is correct.
    """
    global PLAYER

    while True:
        list_player_family()
        user_input = input(f"Are these names correct? {green('[yes/no]')} ")

        # validate if the user selected a valid option
        if validate_yes_no(user_input):
            break

    if user_input[0].lower() == "n":
        # prompt for number to change
        while True:
            list_player_family()
            update_name = input(f"Change which name? {aqua('[1-5]')} ")
            choices = ["1", "2", "3", "4", "5"]

            # validate 1-5
            if validate_menu_input(update_name, choices):
                break

        if update_name == "1":  # wagon leader
            PLAYER.name = ask_name("What is the correct name of the wagon leader? ")  # noqa
        else:  # family members
            PLAYER.family[int(update_name) - 2].name = ask_name(f"What is the correct name for {aqua(player.family[int(update_name) - 2].name)}? ")  # noqa
        confirm_names()


def pick_start_month():
    """
    Ask the user to pick their starting month from:
    March, April, May, June, or July
    """
    global GAME

    while True:
        clear()
        print(green(LINE))
        print(green(CENT("Pick your Departure Month")))
        print(green(LINE))
        print("")
        print(CENT("It is 1848. Your jumping off place for Oregon"))
        print(CENT("is Independence, Missouri. You must decide which"))
        print(CENT("month to leave Independence.\n"))
        print(f'\t\t\t{green("1. ")}{"March"}')
        print(f'\t\t\t{green("2. ")}{"April"}')
        print(f'\t\t\t{green("3. ")}{"May"}')
        print(f'\t\t\t{green("4. ")}{"June"}')
        print(f'\t\t\t{green("5. ")}{"July"}')
        print(f'\t\t\t{green("6. ")}{"Ask for advice"}')

        user_input = input(f"\n\t\tWhat is your choice? {green('[1-6]')} ")
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

    GAME.date = GAME.set_start_date(month)
    return GAME.date


def populate_family():
    """
    Allows the player to choose their own family members,
    or have the members randomly selected for them.
    """
    global PLAYER

    # ask if the player would like random names, or to choose their own
    while True:
        list_player_family()
        print("\tPick your own family names, or randomly selected names?\n")
        print(f'\t\t{green("1. ")}{"Choose my own wagon party"}')
        print(f'\t\t{green("2. ")}{"Randomly selected wagon party"}')

        choose_names = input(f"\n\t\tWhat is your choice? {green('[1-2]')} ")
        choices = ["1", "2"]

        # validate if the user selected a valid option
        if validate_menu_input(choose_names, choices):
            break

    # player's family members (4 other instances of Person)
    for i in range(0, 4):
        list_player_family()
        family_member = Person(None)
        if choose_names == "1":
            # build the player's family of 4 more persons
            family_member.name = ask_name("What is the first name of the next family member? ")  # noqa
        elif choose_names == "2":
            # pick randomly selected names for the player's family
            family_member.name = family_member.get_random_name()
        PLAYER.family.append(family_member)
    list_player_family()

    # confirm if names are correct
    confirm_names()


def matts_store():
    """
    Displays Matt's General Store purchases before leaving Independence.
    """
    global PLAYER, GAME

    clear()
    print(red(LINE))
    print(CENT("Matt's General Store"))
    print(CENT("Independence, Missouri"))
    print(CENT(f"{GAME.date}"))
    print(red(LINE))
    print(f"\t\t\t{red('1. ') + 'Oxen':<50}{'$0.00':>15}")
    print(f"\t\t\t{red('2. ') + 'Food':<50}{'$0.00':>15}")
    print(f"\t\t\t{red('3. ') + 'Clothing':<50}{'$0.00':>15}")
    print(f"\t\t\t{red('4. ') + 'Ammunition':<50}{'$0.00':>15}")
    print(f"\t\t\t{red('5. ') + 'Spare parts':<50}{'$0.00':>15}")
    print(red(LINE))
    print(CENT(f"Total bill: $0.00"))
    print("")
    print(CENT(f"Amount you have: ${PLAYER.cash:.2f}"))
    print("")


def purchase_inventory():
    """
    This is the initial purchase prior to setting off from Independence.
    """
    global PLAYER

    clear()
    print(green(LINE))
    print(green(CENT("Buying Supplies")))
    print(green(LINE))
    print("")
    print(CENT("Before leaving Independence, you should buy"))
    print(CENT(f"equipment and supplies. You have ${PLAYER.cash:.2f} in cash,"))  # noqa
    print(CENT("but you don't have to spend it all now.\n"))
    print(CENT("You can buy whatever you need at Matt's General Store."))
    print("")
    print(green(LINE))
    input(f'{grey(CENT("Press ENTER to continue"))}\n')

    clear()
    print(green(LINE))
    print(green(CENT("Buying Supplies")))
    print(green(LINE))
    print("")
    print(CENT("Hello, I'm Matt. So you're going to Oregon!"))
    print(CENT("I can fix you up with what you need:"))
    print("")
    print("\t\t\t- a team of oxen to pull your wagon")
    print("\t\t\t- clothing for both summer and winter")
    print("\t\t\t- plenty of food for the trip")
    print("\t\t\t- ammunition for your rifles")
    print("\t\t\t- spare parts for your wagon")
    print("")
    print(green(LINE))
    input(f'{grey(CENT("Press ENTER to continue"))}\n')

    matts_store()
    input("pause")


def start_game(profession):
    """
    Player begins defining their game data.
    """
    global PLAYER, GAME

    # initialize a new instance of the Game()
    GAME = Game()
    # initialize a new instance of the Player() with profession
    PLAYER = Player(profession)
    # set the starter cash based on profession
    PLAYER.profession_starter_cash()
    # ask for the player's name
    PLAYER.name = ""
    list_player_family()
    PLAYER.name = ask_name("What is the first name of the wagon leader? ")  # noqa

    # generate the player's other 4 family members
    populate_family()

    # decide when to leave
    pick_start_month()

    # buy supplies
    purchase_inventory()

    # print(f"Name: {PLAYER.name}\nProfession: {PLAYER.profession}\nCash: ${PLAYER.cash}")  # noqa
