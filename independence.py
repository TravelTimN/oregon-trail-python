import time
from colors import aqua, green, grey, pink, red
from game import start_cycle, end_game
from learn import learn_about_months, learn_about_professions
from objects import Game, Inventory, Person, Player
from utils import clear, LINE, CENT, generate_title
from validators import (
    validate_choice, validate_name, validate_yes_no, validate_minmax
)


PLAYER = GAME = INVENTORY = None


def pick_profession():
    """
    Creates a menu for player to pick their profession.
    """
    while True:
        generate_title(green, "Pick your Profession")

        print("\tMany kinds of people made the trip to Oregon.")
        time.sleep(0.05)
        print("\n\tYou may:\n")
        time.sleep(0.05)
        print(f'\t\t{green("1. ")}{"Be a banker from Boston"}')
        time.sleep(0.05)
        print(f'\t\t{green("2. ")}{"Be a carpenter from Ohio"}')
        time.sleep(0.05)
        print(f'\t\t{green("3. ")}{"Be a farmer from Illinois"}')
        time.sleep(0.05)
        print(f'\t\t{green("4. ")}{"Find out the differences between these choices"}')  # noqa
        # time.sleep(0.05)

        user_input = input(f"\n\t\tWhat is your choice? {green('[1-4]')} ").strip()  # noqa
        choices = ["1", "2", "3", "4"]

        # validate if the user selected a valid option
        if validate_choice(user_input, choices):
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


def ask_name(question):
    """
    Helper function to ask for player name, and all family names
    """
    while True:
        user_input = input(question).strip()  # noqa

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

    generate_title(green, "Your Wagon Party")
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
        user_input = input(f"Are these names correct? {green('[yes/no]')} ").strip()  # noqa

        # validate if the user selected a valid option
        if validate_yes_no(user_input):
            break

    if user_input[0].lower() == "n":
        # prompt for number to change
        while True:
            list_player_family()
            update_name = input(f"Change which name? {aqua('[1-5]')} ").strip()  # noqa
            choices = ["1", "2", "3", "4", "5"]

            # validate 1-5
            if validate_choice(update_name, choices):
                break

        if update_name == "1":  # wagon leader
            PLAYER.name = ask_name("What is the correct name of the wagon leader? ")  # noqa
        else:  # family members
            PLAYER.family[int(update_name) - 2].name = ask_name(f"What is the correct name for {aqua(PLAYER.family[int(update_name) - 2].name)}? ")  # noqa
        confirm_names()

    # update the total number of persons alive
    PLAYER.get_persons_alive()


def pick_start_month():
    """
    Ask the user to pick their starting month from:
    March, April, May, June, or July
    """
    global GAME

    while True:
        generate_title(green, "Pick your Departure Month")
        print(CENT("It is 1848. Your jumping off place for Oregon"))
        time.sleep(0.05)
        print(CENT("is Independence, Missouri. You must decide which"))
        time.sleep(0.05)
        print(CENT("month to leave Independence.\n"))
        time.sleep(0.05)
        print(f'\t\t\t{green("1. ")}{"March"}')
        time.sleep(0.05)
        print(f'\t\t\t{green("2. ")}{"April"}')
        time.sleep(0.05)
        print(f'\t\t\t{green("3. ")}{"May"}')
        time.sleep(0.05)
        print(f'\t\t\t{green("4. ")}{"June"}')
        time.sleep(0.05)
        print(f'\t\t\t{green("5. ")}{"July"}')
        time.sleep(0.05)
        print(f'\t\t\t{green("6. ")}{"Ask for advice"}')
        time.sleep(0.05)

        user_input = input(f"\n\t\tWhat is your choice? {green('[1-6]')} ").strip()  # noqa
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

        choose_names = input(f"\n\t\tWhat is your choice? {green('[1-2]')} ").strip()  # noqa
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


def matts_store_buy_item(item, cost, text, question, min, max):
    """
    Helper function to buy items from Matt's General Store.
    """
    global PLAYER, INVENTORY

    while True:
        clear()
        print(red(LINE))
        print(CENT("Matt's General Store"))
        print(CENT("Independence, Missouri"))
        print(red(LINE))
        print(text)
        print("")
        print(CENT(f"Bill so far: ${PLAYER.bill:.2f}"))

        buy_item = input(question).strip()  # noqa

        # validate if the user selected a valid option
        if validate_minmax(buy_item, min, max):
            break

    # players who return for more of same item, reset back to 0 initially
    existing_item = getattr(INVENTORY, item)
    if existing_item != 0:
        setattr(INVENTORY, item, 0)
        # deduct from the current bill
        if item == "oxen":
            PLAYER.bill -= (int(existing_item) / 2) * cost
        elif item == "bullets":
            PLAYER.bill -= (int(existing_item) / 20) * cost
        else:
            PLAYER.bill -= int(existing_item) * cost

    # increment player bill with the item * cost
    PLAYER.bill += int(buy_item) * cost
    remaining = PLAYER.cash - PLAYER.bill
    if remaining >= 0:  # player has money remaining
        # update inventory/bill
        if item == "oxen":
            setattr(INVENTORY, item, int(buy_item) * 2)
        elif item == "bullets":
            setattr(INVENTORY, item, int(buy_item) * 20)
        else:
            setattr(INVENTORY, item, int(buy_item))
    else:
        # player cannot afford the item/quantity
        PLAYER.bill -= int(buy_item) * cost  # give them back their money
        remaining = PLAYER.cash + PLAYER.bill
        setattr(INVENTORY, item, existing_item)  # set back to original qty
        # deduct the value from the current bill
        if item == "oxen":
            PLAYER.bill += (int(existing_item) / 2) * cost
        elif item == "bullets":
            PLAYER.bill += (int(existing_item) / 20) * cost
        else:
            PLAYER.bill += int(existing_item) * cost
        # display error message
        print(red(CENT(f"You cannot afford {buy_item} {item}")))
        input(f'{grey(CENT("Press ENTER to continue"))}\n')


def matts_store_receipt():
    """
    Displays Matt's General Store purchases before leaving Independence.
    """
    global PLAYER, GAME, INVENTORY

    while True:
        oxen = (INVENTORY.oxen / 2) * 40
        food = INVENTORY.food * 0.2
        clothing = INVENTORY.clothing * 10
        bullets = (INVENTORY.bullets / 20) * 2
        spare_parts = INVENTORY.wheels + INVENTORY.axles + INVENTORY.tongues
        spares_cost = spare_parts * 10
        remaining = PLAYER.cash - PLAYER.bill

        clear()
        print(red(LINE))
        time.sleep(0.05)
        print(CENT("Matt's General Store"))
        time.sleep(0.05)
        print(CENT("Independence, Missouri"))
        time.sleep(0.05)
        print(CENT(f"{GAME.date_string}"))
        time.sleep(0.05)
        print(red(LINE))
        time.sleep(0.05)
        print(f"\t\t\t{red('1. ') + 'Oxen':<60}${oxen:.2f} ({INVENTORY.oxen})")
        time.sleep(0.05)
        print(f"\t\t\t{red('2. ') + 'Food':<60}${food:.2f} ({INVENTORY.food})")
        time.sleep(0.05)
        print(f"\t\t\t{red('3. ') + 'Clothing':<60}${clothing:.2f} ({INVENTORY.clothing})")  # noqa
        time.sleep(0.05)
        print(f"\t\t\t{red('4. ') + 'Ammunition':<60}${bullets:.2f} ({INVENTORY.bullets})")  # noqa
        time.sleep(0.05)
        print(f"\t\t\t{red('5. ') + 'Spare parts':<60}${spares_cost:.2f} ({spare_parts})")  # noqa
        time.sleep(0.05)
        print(f"\t\t\t{red('6. ') + 'Leave Store'}")
        time.sleep(0.05)
        print(red(LINE))
        time.sleep(0.05)
        print(f"\t\t\t{'Total bill:':<26}${PLAYER.bill:>2.2f}")
        time.sleep(0.05)
        print(f"\t\t\t{'Amount remaining:':<26}${remaining:>2.2f}")  # noqa
        time.sleep(0.05)

        user_input = input(f"\n\t\t\tBuy item, or leave store? {red('[1-6]')} ").strip()  # noqa
        choices = ["1", "2", "3", "4", "5", "6"]

        # validate if the user selected a valid option
        if validate_choice(user_input, choices):

            if user_input == "1":  # oxen
                cost = 40.00
                text = (f"""
{CENT("There are 2 oxen in a yoke; I recommend at least 3 yoke.")}
{CENT(f"I charge ${cost:.2f} a yoke.")}""")
                question = f"\n\t\t\tHow many yoke do you want? {red('[1-9]')} "  # noqa
                matts_store_buy_item("oxen", cost, text, question, 1, 9)
            elif user_input == "2":  # food
                cost = 0.20
                text = (f"""
{CENT("I recommend you take at least 200 pounds of food")}
{CENT("for each person in your family. I see that you have")}
{CENT("5 people in all. You'll need flour, sugar, bacon,")}
{CENT(f"and coffee. My price is ${cost:.2f} a pound.")}""")
                question = f"\n\t\tHow many pounds of food do you want? {red('[1000-2000]')} "  # noqa
                matts_store_buy_item("food", cost, text, question, 1000, 2000)
            elif user_input == "3":  # clothing
                cost = 10.00
                text = (f"""
{CENT("You'll need warm clothing in the mountains.")}
{CENT("I recommend taking at least 2 sets of clothes")}
{CENT(f"per person. Each set is ${cost:.2f}.")}""")
                question = f"\n\t\tHow many sets of clothes do you want? {red('[10-99]')} "  # noqa
                matts_store_buy_item("clothing", cost, text, question, 10, 99)
            elif user_input == "4":  # bullets
                cost = 2.00
                text = (f"""
{CENT("I sell ammunition in boxes of 20 bullets.")}
{CENT(f"Each box costs ${cost:.2f}.")}""")
                question = f"\n\t\t\tHow many boxes do you want? {red('[1-99]')} "  # noqa
                matts_store_buy_item("bullets", cost, text, question, 1, 99)
            elif user_input == "5":  # spare parts
                parts = ["wheels", "axles", "tongues"]
                cost = 10
                text = (f"""
{CENT("It's a good idea to have a few spare parts")}
{CENT("for your wagon. Here are the prices:")}

{CENT(f"wagon wheel  - ${cost} each")}
{CENT(f"wagon axle   - ${cost} each")}
{CENT(f"wagon tongue - ${cost} each")}""")
                for part in parts:
                    question = f"\n\t\t\tHow many wagon {part}? {red('[0-3]')} "  # noqa
                    matts_store_buy_item(part, cost, text, question, 0, 3)
            elif user_input == "6":

                generate_title(pink, "Talking to Matt")
                if INVENTORY.oxen == 0 or INVENTORY.food == 0 or INVENTORY.clothing == 0 or INVENTORY.bullets == 0:  # noqa
                    if INVENTORY.oxen == 0:
                        msg = "Don't forget, you'll need oxen to pull your wagon."  # noqa
                    elif INVENTORY.food == 0:
                        msg = "Although you can hunt, there's no guarantee you'll get any food."  # noqa
                    elif INVENTORY.clothing == 0:
                        msg = "You'll need extra layers of clothing to stay warm in the mountains."  # noqa
                    elif INVENTORY.bullets == 0:
                        msg = "Ammunition is necessary for hunting, and against potential bandits."  # noqa
                    print(CENT(msg))
                    print("")
                    print(pink(LINE))
                    input(f'{grey(CENT("Press ENTER to continue"))}\n')
                else:
                    PLAYER.cash = remaining  # deduce the purchases
                    PLAYER.bill = 0  # reset bill for next shop at forts
                    print(CENT("Well then, you're ready to start. Good luck!"))
                    time.sleep(0.05)
                    print(CENT("You have a long and difficult journey ahead of you."))  # noqa
                    time.sleep(0.05)
                    print("")
                    time.sleep(0.05)
                    print(pink(LINE))
                    time.sleep(0.05)
                    input(f'{grey(CENT("Press ENTER to continue"))}\n')
                    break


def purchase_inventory():
    """
    This is the initial purchase prior to setting off from Independence.
    """
    global PLAYER

    generate_title(green, "Buying Supplies")
    print(CENT("Before leaving Independence, you should buy"))
    time.sleep(0.05)
    print(CENT(f"equipment and supplies. You have ${PLAYER.cash:.2f} in cash,"))  # noqa
    time.sleep(0.05)
    print(CENT("but you don't have to spend it all now.\n"))
    time.sleep(0.05)
    print(CENT("You can buy whatever you need at Matt's General Store."))
    time.sleep(0.05)
    print("")
    time.sleep(0.05)
    print(green(LINE))
    time.sleep(0.05)
    input(f'{grey(CENT("Press ENTER to continue"))}\n')

    generate_title(pink, "Talking to Matt")
    print(CENT("Hello, I'm Matt. So you're going to Oregon!"))
    time.sleep(0.05)
    print(CENT("I can fix you up with what you need:"))
    time.sleep(0.05)
    print("")
    time.sleep(0.05)
    print("\t\t\t- a team of oxen to pull your wagon")
    time.sleep(0.05)
    print("\t\t\t- clothing for both summer and winter")
    time.sleep(0.05)
    print("\t\t\t- plenty of food for the trip")
    time.sleep(0.05)
    print("\t\t\t- ammunition for your rifles")
    time.sleep(0.05)
    print("\t\t\t- spare parts for your wagon")
    time.sleep(0.05)
    print("")
    time.sleep(0.05)
    print(pink(LINE))
    time.sleep(0.05)
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
    PLAYER = Player(profession, "")
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

    # start the game (loading the wagon)
    generate_title(green, "Loading the Wagon")
    print(CENT("Please Wait"))
    time.sleep(0.05)
    print("")
    time.sleep(0.05)
    print(CENT("Supplies and oxen being loaded with your wagon."))
    time.sleep(0.05)
    print("")
    time.sleep(0.05)
    print(CENT("Safe travels!"))
    time.sleep(0.05)
    print("")
    time.sleep(0.05)
    print(green(LINE))
    time.sleep(5)
    # start the game cycle
    start_cycle(GAME, INVENTORY, PLAYER)


def konami():
    """
    This is used for faster testing while in development mode.
    TODO: update this to perhaps only give the player a cash bonus?
    """
    GAME = Game()
    INVENTORY = Inventory()
    PLAYER = Player("banker", "Tim")
    PLAYER.profession_starter_cash()
    for i in range(0, 4):
        family_member = Person(None)
        family_member.name = family_member.get_random_name()
        PLAYER.family.append(family_member)
    PLAYER.get_persons_alive()
    GAME.date = GAME.set_start_date(3)
    INVENTORY.oxen = 18
    INVENTORY.food = 2000
    INVENTORY.clothing = 50
    INVENTORY.bullets = 200
    INVENTORY.wheels = 3
    INVENTORY.axles = 3
    INVENTORY.tongues = 3
    PLAYER.cash = 230.00
    GAME.get_current_location()
    GAME.get_current_weather()
    start_cycle(GAME, INVENTORY, PLAYER)
