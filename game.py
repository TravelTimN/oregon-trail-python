import sys
import time
from animation import animate_wagon
from colors import green, red
# from landmarks import landmarks
from utils import CENT, clear, generate_title, generate_title_date, LINE
from validators import validate_choice


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


def start_cycle(GAME, INVENTORY, PLAYER):
    """
    Starts the main game play in Independence.
    """
    while True:
        generate_title_date(green, GAME.current_location, GAME.date)

        print(f"\t\t\t{'Weather:':<24}{GAME.weather}")
        print(f"\t\t\t{'Health:':<24}{PLAYER.health}")
        print(f"\t\t\t{'Pace:':<24}{PLAYER.pace}")
        print(f"\t\t\t{'Rations:':<24}{PLAYER.rations}")
        print(green(LINE))

        print("\tYou may:\n")
        print(f'\t\t{green("1. ")}{"Continue trail"}')
        print(f'\t\t{green("2. ")}{"Check supplies"}')
        print(f'\t\t{green("3. ")}{"Look at map"}')
        print(f'\t\t{green("4. ")}{"Change pace"}')
        print(f'\t\t{green("5. ")}{"Change food rations"}')
        print(f'\t\t{green("6. ")}{"Stop to rest"}')
        print(f'\t\t{green("7. ")}{"Attempt to trade"}')
        print(f'\t\t{green("8. ")}{"Talk to people"}')

        user_input = input(f"\n\t\tWhat is your choice? {green('[1-8]')} ")
        choices = ["1", "2", "3", "4", "5", "6", "7", "8"]

        # validate if the user selected a valid option
        if validate_choice(user_input, choices):

            clear()
            if user_input == "1":  # continue on trail
                animate_wagon()
                print("Continue on trail")
                input("pause")
            elif user_input == "2":  # check supplies
                print("Check supplies")
                input("pause")
            elif user_input == "3":  # look at map
                print("Look at map")
                input("pause")
            elif user_input == "4":  # change pace
                print("Change pace")
                input("pause")
            elif user_input == "5":  # change food rations
                print("Change food rations")
                input("pause")
            elif user_input == "6":  # stop to rest
                print("Stop to rest")
                input("pause")
            elif user_input == "7":  # attempt to trade
                print("Attempt to trade")
                input("pause")
            elif user_input == "8":  # talk to people
                print("Talk to people")
                input("pause")
