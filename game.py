import sys
import time
from colors import brown, green, peach, pink
from objects import Person, Player
from utils import clear, LINE, CENT
from validators import validate_menu_input, validate_name


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
    print(f"\t{peach('1.')} {player.name} (you)")
    for i, person in enumerate(player.family):
        print(f"\t{peach(str(i+2)+'.')} {person.name}")
    print("")


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
    print("")
    player.name = ask_name(player, "What is the first name of the wagon leader? ")  # noqa

    # build the player's family of 4 more persons
    for i in range(0, 4):
        list_player_family(player)
        family_member = Person(None)
        family_member.name = ask_name(player, "What is the first name of the next family member? ")  # noqa
        player.family.append(family_member)
    list_player_family(player)

    print(f"Name: {player.name}\nProfession: {player.profession}\nCash: ${player.cash}")  # noqa
