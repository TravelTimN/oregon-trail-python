import sys
import time
from animation import animate_wagon
from colors import green, grey, pink, red, yellow
from landmarks import landmarks
from learn import learn_about_pace
from utils import CENT, clear, generate_title, generate_title_date, LINE
from validators import validate_choice


def end_game():
    """
    Function to completely stop the app running.
    """
    time.sleep(0.05)
    print(red(LINE))
    time.sleep(0.05)
    print(CENT("Thanks for playing The Python Oregon Trail."))
    time.sleep(0.05)
    print(CENT("Hopefully you didn't die of dysentery!"))
    time.sleep(0.05)
    print(red(LINE), "\n")
    time.sleep(1)
    sys.exit()


def check_supplies(INVENTORY, PLAYER):
    """
    Displays the user's oxen, clothes, bullets, spare parts, food, and cash.
    """
    generate_title(yellow, "Your Supplies")
    print(f"\t\t\t{'oxen':<24}{INVENTORY.oxen}")
    time.sleep(0.05)
    print(f"\t\t\t{'sets of clothing':<24}{INVENTORY.clothing}")
    time.sleep(0.05)
    print(f"\t\t\t{'bullets':<24}{INVENTORY.bullets}")
    time.sleep(0.05)
    print(f"\t\t\t{'wagon wheels':<24}{INVENTORY.wheels}")
    time.sleep(0.05)
    print(f"\t\t\t{'wagon axles':<24}{INVENTORY.axles}")
    time.sleep(0.05)
    print(f"\t\t\t{'wagon tongues':<24}{INVENTORY.tongues}")
    time.sleep(0.05)
    print(f"\t\t\t{'pounds of food':<24}{INVENTORY.food}")
    time.sleep(0.05)
    print(f"\t\t\t{'money left':<24}${PLAYER.cash:.2f}")
    time.sleep(0.05)
    print("")
    time.sleep(0.05)
    print(yellow(LINE))
    time.sleep(0.05)
    input(f'{grey(CENT("Press ENTER to continue"))}\n')


def show_map():
    """
    Weak attempt to create a visible map representation.
    TODO: needs work!!!
    """
    generate_title(yellow, "Map of the Oregon Trail")
    time.sleep(0.05)
    print("Start ☆\t\tFort 🞓\t\tRiver ⌇⌇\tOther ▪\t\tEnd ✪\n")
    time.sleep(0.05)
    print("☆  Independence, Missouri")
    time.sleep(0.05)
    print("┗━❱ ⌇⌇ Kansas River Crossing")
    time.sleep(0.05)
    print("   ┗━❱ ⌇⌇ Big Blue River Crossing")
    time.sleep(0.05)
    print("      ┗━❱ 🞓  Fort Kearney")
    time.sleep(0.05)
    print("         ┗━❱ ▪ Chimney Rock")
    time.sleep(0.05)
    print("            ┗━❱ 🞓  Fort Laramie")
    time.sleep(0.05)
    print("               ┗━❱ ▪ Independence Rock")
    time.sleep(0.05)
    print("               ┗━❱ ▪ South Pass")
    time.sleep(0.05)
    print("                  ┗━❱ ⌇⌇ Green River Crossing")
    time.sleep(0.05)
    print("                  ┗━❱ 🞓  Fort Bridger")
    time.sleep(0.05)
    print("                     ┗━❱ ▪ Soda Springs")
    time.sleep(0.05)
    print("                        ┗━❱ 🞓  Fort Hall")
    time.sleep(0.05)
    print("                           ┗━❱ ⌇⌇ Snake River Crossing")
    time.sleep(0.05)
    print("                              ┗━❱ 🞓  Fort Boise")
    time.sleep(0.05)
    print("                                 ┗━❱ ▪ Blue Mountains")
    time.sleep(0.05)
    print("                                    ┗━❱ 🞓  Fort Walla Walla")
    time.sleep(0.05)
    print("                                    ┗━❱ ▪ The Dalles")
    time.sleep(0.05)
    print("                                       ┗━❱ ✪ Willamette Valley, Oregon\n")  # noqa
    time.sleep(0.05)
    print(yellow(LINE))
    time.sleep(0.05)
    input(f'{grey(CENT("Press ENTER to continue"))}\n')


def change_pace(PLAYER):
    """
    Allows player to change their pace.
    Options: steady || strenuous || grueling
    """
    while True:
        generate_title(green, "Change Pace")

        print(f"\tCurrent Pace: {green(PLAYER.pace)}\n")
        time.sleep(0.05)
        print("\tThe pace at which you travel can change.")
        time.sleep(0.05)
        print("\tYour choices are:\n")
        time.sleep(0.05)
        print(f'\t\t{green("1. ")}{"a steady pace"}')
        time.sleep(0.05)
        print(f'\t\t{green("2. ")}{"a strenuous pace"}')
        time.sleep(0.05)
        print(f'\t\t{green("3. ")}{"a grueling pace"}')
        time.sleep(0.05)
        print(f'\t\t{green("4. ")}{"find out what these different paces mean"}')  # noqa
        time.sleep(0.05)

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


def change_ration(PLAYER):
    """
    Allows player to change their food rations.
    Options: filling || meager || bear bones
    """
    while True:
        generate_title(green, "Change Food Rations")

        print(f"\tCurrent Rations: {green(PLAYER.rations)}\n")
        time.sleep(0.05)
        print("\tThe amount of food the people in your party eat each day can change.")  # noqa
        time.sleep(0.05)
        print("\tYour choices are:\n")
        time.sleep(0.05)
        print(f'\t\t{green("1. ")}{"filling - meals are large and generous."}')
        time.sleep(0.05)
        print(f'\t\t{green("2. ")}{"meager - meals are small, but adequate."}')
        time.sleep(0.05)
        print(f'\t\t{green("3. ")}{"bear bones - meals are very small; everyone stays hungry."}')  # noqa
        time.sleep(0.05)

        user_input = input(f"\n\t\tWhat is your choice? {green('[1-3]')} ")
        choices = ["1", "2", "3"]

        # validate if the user selected a valid option
        if validate_choice(user_input, choices):
            break

    if user_input == "1":
        PLAYER.rations = "filling"
    elif user_input == "2":
        PLAYER.rations = "meager"
    elif user_input == "3":
        PLAYER.rations = "bear bones"


def start_cycle(GAME, INVENTORY, PLAYER):
    """
    Starts the main game play in Independence.
    """
    # handle new/existing chats to people
    talked_to_people = False
    convos = []

    # current location id (eg: L01)
    current_location_id = GAME.current_location_id
    # current location (full instance)
    current_location = next(filter(lambda landmark : landmark["id"] == current_location_id, landmarks))  # noqa
    next_destination_id = current_location["next_destination_id"]

    while True:
        generate_title_date(green, GAME.current_location_name, GAME.date)

        print(f"\t\t\t{'Weather:':<24}{GAME.weather}")
        time.sleep(0.05)
        print(f"\t\t\t{'Health:':<24}{PLAYER.health}")
        time.sleep(0.05)
        print(f"\t\t\t{'Pace:':<24}{PLAYER.pace}")
        time.sleep(0.05)
        print(f"\t\t\t{'Rations:':<24}{PLAYER.rations}")
        time.sleep(0.05)
        print(green(LINE))
        time.sleep(0.05)

        print("\tYou may:\n")
        time.sleep(0.05)
        print(f'\t\t{green("1. ")}{"Continue trail"}')
        time.sleep(0.05)
        print(f'\t\t{green("2. ")}{"Check supplies"}')
        time.sleep(0.05)
        print(f'\t\t{green("3. ")}{"Look at map"}')
        time.sleep(0.05)
        print(f'\t\t{green("4. ")}{"Change pace"}')
        time.sleep(0.05)
        print(f'\t\t{green("5. ")}{"Change food rations"}')
        time.sleep(0.05)
        print(f'\t\t{green("6. ")}{"Stop to rest"}')
        time.sleep(0.05)
        print(f'\t\t{green("7. ")}{"Attempt to trade"}')
        time.sleep(0.05)
        print(f'\t\t{green("8. ")}{"Talk to people"}')
        time.sleep(0.05)
        if current_location["category"] == "start" or current_location["category"] == "fort":  # noqa
            # Independence and Forts have options to buy supplies
            print(f'\t\t{green("9. ")}{"Buy supplies"}')
            time.sleep(0.05)

            user_input = input(f"\n\t\tWhat is your choice? {green('[1-9]')} ")
            time.sleep(0.05)
            choices = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        else:
            user_input = input(f"\n\t\tWhat is your choice? {green('[1-8]')} ")
            time.sleep(0.05)
            choices = ["1", "2", "3", "4", "5", "6", "7", "8"]

        # validate if the user selected a valid option
        if validate_choice(user_input, choices):

            clear()
            if user_input == "1":  # continue on trail
                animate_wagon()
                print("Continue on trail")
                input("pause")
                talked_to_people = False
                # TODO: break

            elif user_input == "2":  # check supplies
                check_supplies(INVENTORY, PLAYER)

            elif user_input == "3":  # look at map
                show_map()

            elif user_input == "4":  # change pace
                change_pace(PLAYER)

            elif user_input == "5":  # change food rations
                change_ration(PLAYER)

            elif user_input == "6":  # stop to rest
                print("Stop to rest")
                input("pause")

            elif user_input == "7":  # attempt to trade
                print("Attempt to trade")
                input("pause")

            elif user_input == "8":  # talk to people

                # first time talking to people, randomize conversation order
                if not talked_to_people:
                    convos = []  # reset
                    shuffle_conversations = GAME.shuffle_conversations(current_location["conversations"])  # noqa
                    talked_to_people = True
                    convos.extend(shuffle_conversations)

                generate_title(pink, f"Talking to {convos[0]['person']}")
                print(CENT(convos[0]["speech"]))
                print("")
                print(pink(LINE))
                input(f'{grey(CENT("Press ENTER to continue"))}\n')
                GAME.talk_to_people(convos)  # pop + append convo to end
