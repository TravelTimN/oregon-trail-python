import sys
import time
from colors import aqua, brown, green, grey, peach, pink, red, yellow
from learn import learn_about_months
from objects import Game, Inventory, Person, Player
from utils import clear, LINE, CENT
from validators import (
    validate_choice, validate_name, validate_yes_no, validate_minmax
)


PLAYER = GAME = INVENTORY = None


def end_game():
    """
    Function to completely stop the app running.
    """
    time.sleep(0.25)
    print(red(LINE))
    time.sleep(0.25)
    print(CENT("Thanks for playing The Python Oregon Trail."))
    time.sleep(0.25)
    print(CENT("Hopefully you didn't die of dysentery!"))
    time.sleep(0.25)
    print(red(LINE), "\n")
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
            if validate_choice(update_name, choices):
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
        if validate_choice(user_input, choices):
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
        if validate_choice(choose_names, choices):
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


def matts_store_buy_oxen():
    """
    Buying oxen (2 per yoke) from Matt's General Store.
    """
    global PLAYER, INVENTORY

    cost_yoke = 40.00

    while True:
        clear()
        print(red(LINE))
        print(CENT("Matt's General Store"))
        print(CENT("Independence, Missouri"))
        print(red(LINE))
        print("")
        print(CENT("There are 2 oxen in a yoke; I recommend at least 3 yoke."))
        print(CENT(f"I charge ${cost_yoke:.2f} a yoke."))
        print("")
        print(CENT(f"Bill so far: ${PLAYER.bill:.2f}"))

        buy_oxen = input(f"\n\t\t\tHow many yoke do you want? {red('[1-9]')} ")

        # validate if the user selected a valid option
        if validate_minmax(buy_oxen, 1, 9):
            break

    # players who return for more oxen, reset back to 0 initially
    existing_oxen = INVENTORY.oxen
    if existing_oxen != 0:
        INVENTORY.oxen = 0
        PLAYER.bill -= (int(existing_oxen) / 2) * cost_yoke
    # update inventory/bill
    INVENTORY.oxen = int(buy_oxen) * 2
    PLAYER.bill += int(buy_oxen) * cost_yoke


def matts_store_receipt():
    """
    Displays Matt's General Store purchases before leaving Independence.
    """
    global PLAYER, GAME, INVENTORY

    while True:
        oxen = (INVENTORY.oxen / 2) * 40
        remaining = PLAYER.cash - PLAYER.bill

        clear()
        print(red(LINE))
        print(CENT("Matt's General Store"))
        print(CENT("Independence, Missouri"))
        print(CENT(f"{GAME.date}"))
        print(red(LINE))
        print(f"\t\t\t{red('1. ') + 'Oxen':<60}${oxen:.2f}")
        print(f"\t\t\t{red('2. ') + 'Food':<60}${'0.00'}")
        print(f"\t\t\t{red('3. ') + 'Clothing':<60}${'0.00'}")
        print(f"\t\t\t{red('4. ') + 'Ammunition':<60}${'0.00'}")
        print(f"\t\t\t{red('5. ') + 'Spare parts':<60}${'0.00'}")
        print(f"\t\t\t{red('6. ') + 'Leave Store'}")
        print(red(LINE))
        print(f"\t\t\t{'Total bill:':<26}${PLAYER.bill:>2.2f}")
        print(f"\t\t\t{'Amount you have:':<26}${remaining:>2.2f}")

        user_input = input(f"\n\t\t\tBuy item, or leave store? {red('[1-6]')} ")  # noqa
        choices = ["1", "2", "3", "4", "5", "6"]

        # validate if the user selected a valid option
        if validate_choice(user_input, choices):
            # break

            if user_input == "1":
                matts_store_buy_oxen()
            elif user_input == "6":
                break


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

    # start generating Matt's shopping receipt
    matts_store_receipt()


def start_game(profession):
    """
    Player begins defining their game data.
    """
    global PLAYER, GAME, INVENTORY

    # initialize a new instance of the Game() and Inventory()
    GAME = Game()
    INVENTORY = Inventory()
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
