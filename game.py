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


def check_supplies(INVENTORY, PLAYER):
    """
    Displays the user's oxen, clothes, bullets, spare parts, food, and cash.
    """
    generate_title(yellow, "Your Supplies")
    print(f"\t\t\t{'oxen':<24}{INVENTORY.oxen}")
    print(f"\t\t\t{'sets of clothing':<24}{INVENTORY.clothing}")
    print(f"\t\t\t{'bullets':<24}{INVENTORY.bullets}")
    print(f"\t\t\t{'wagon wheels':<24}{INVENTORY.wheels}")
    print(f"\t\t\t{'wagon axles':<24}{INVENTORY.axles}")
    print(f"\t\t\t{'wagon tongues':<24}{INVENTORY.tongues}")
    print(f"\t\t\t{'pounds of food':<24}{INVENTORY.food}")
    print(f"\t\t\t{'money left':<24}${PLAYER.cash:.2f}")
    print("")
    print(yellow(LINE))
    input(f'{grey(CENT("Press ENTER to continue"))}\n')


def show_map():
    """
    Weak attempt to create a visible map representation.
    TODO: needs work!!!
    """
    generate_title(yellow, "Map of the Oregon Trail")
    print("Start ☆\t\tFort 🞓\t\tRiver ⌇⌇\tOther ▪\t\tEnd ✪\n")
    print("☆  Independence, Missouri")
    print("┗━❱ ⌇⌇ Kansas River Crossing")
    print("   ┗━❱ ⌇⌇ Big Blue River Crossing")
    print("      ┗━❱ 🞓  Fort Kearney")
    print("         ┗━❱ ▪ Chimney Rock")
    print("            ┗━❱ 🞓  Fort Laramie")
    print("               ┗━❱ ▪ Independence Rock")
    print("               ┗━❱ ▪ South Pass")
    print("                  ┗━❱ ⌇⌇ Green River Crossing")
    print("                  ┗━❱ 🞓  Fort Bridger")
    print("                     ┗━❱ ▪ Soda Springs")
    print("                        ┗━❱ 🞓  Fort Hall")
    print("                           ┗━❱ ⌇⌇ Snake River Crossing")
    print("                              ┗━❱ 🞓  Fort Boise")
    print("                                 ┗━❱ ▪ Blue Mountains")
    print("                                    ┗━❱ 🞓  Fort Walla Walla")
    print("                                    ┗━❱ ▪ The Dalles")
    print("                                       ┗━❱ ✪ Willamette Valley, Oregon\n")  # noqa
    print(yellow(LINE))
    input(f'{grey(CENT("Press ENTER to continue"))}\n')


def change_pace(PLAYER):
    """
    Allows player to change their pace.
    Options: steady || strenuous || grueling
    """
    while True:
        generate_title(green, "Change Pace")

        print(f"\tCurrent Pace: {green(PLAYER.pace)}\n")
        print("\tThe pace at which you travel can change.")
        print("\tYour choices are:\n")
        print(f'\t\t{green("1. ")}{"a steady pace"}')
        print(f'\t\t{green("2. ")}{"a strenuous pace"}')
        print(f'\t\t{green("3. ")}{"a grueling pace"}')
        print(f'\t\t{green("4. ")}{"find out what these different paces mean"}')  # noqa

        user_input = input(f"\n\t\tWhat is your choice? {green('[1-4]')} ")
        choices = ["1", "2", "3", "4"]

        # validate if the user selected a valid option
        if validate_choice(user_input, choices):

            if user_input == "1":
                PLAYER.pace = "steady"
                break
            elif user_input == "2":
                PLAYER.pace = "strenuous"
                break
            elif user_input == "3":
                PLAYER.pace = "grueling"
                break
            elif user_input == "4":
                learn_about_pace()


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
