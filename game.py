import math
import random
import sys
import time
from art import animate_wagon, static_wagon
from colors import green, grey, pink, red, yellow
from learn import learn_about_pace
import trades
from utils import CENT, clear, generate_title, generate_title_date, LINE
from validators import validate_choice, validate_minmax, validate_yes_no


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


def check_supplies(Inventory, Player):
    """
    Displays the user's oxen, clothes, bullets, spare parts, food, and cash.
    """
    generate_title(yellow, "Your Supplies")
    print(f"\t\t\t{'oxen':<24}{Inventory.oxen}")
    time.sleep(0.05)
    print(f"\t\t\t{'sets of clothing':<24}{Inventory.clothing}")
    time.sleep(0.05)
    print(f"\t\t\t{'bullets':<24}{Inventory.bullets}")
    time.sleep(0.05)
    print(f"\t\t\t{'wagon wheels':<24}{Inventory.wheels}")
    time.sleep(0.05)
    print(f"\t\t\t{'wagon axles':<24}{Inventory.axles}")
    time.sleep(0.05)
    print(f"\t\t\t{'wagon tongues':<24}{Inventory.tongues}")
    time.sleep(0.05)
    print(f"\t\t\t{'pounds of food':<24}{Inventory.food}")
    time.sleep(0.05)
    print(f"\t\t\t{'money left':<24}${Player.cash:.2f}")
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


def change_pace(Player):
    """
    Allows player to change their pace.
    Options: steady || strenuous || grueling
    """
    while True:
        generate_title(green, "Change Pace")

        print(f"\tCurrent Pace: {green(Player.pace)}\n")
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
                Player.pace = "steady"
                Player.update_pace()
                break
            elif user_input == "2":
                Player.pace = "strenuous"
                Player.update_pace()
                break
            elif user_input == "3":
                Player.pace = "grueling"
                Player.update_pace()
                break
            elif user_input == "4":
                learn_about_pace()


def change_ration(Player):
    """
    Allows player to change their food rations.
    Options: filling || meager || bear bones
    """
    while True:
        generate_title(green, "Change Food Rations")

        print(f"\tCurrent Rations: {green(Player.rations)}\n")
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
        Player.rations = "filling"
    elif user_input == "2":
        Player.rations = "meager"
    elif user_input == "3":
        Player.rations = "bear bones"
    Player.update_rations()


def cycle_one_day(Game, Inventory, Player, is_rest_day, is_trade_day, show_wagon, n):  # noqa
    """
    One day's cycle.
    - ✅ increment day on calendar
    - ✅ deduct food rations
    - ✅ travel N-miles (if not resting)
    - ✅ weather cycle
    - ❌ misfortunes / accidents
    - ✅❌ decrement health (in progress - accidents/diseases TBC)
    """
    current_location = Game.get_current_location()

    # each day, health value is improved by 10% naturally
    Player.health_points -= round(Player.health_points * 0.1, 1)

    # 50% chance that the weather stays the same as previous day's weather
    change_weather_choices = ["yes", "no"]
    weather_weights = [0.5, 0.5]
    change_weather = random.choices(change_weather_choices, weather_weights)
    if change_weather[0] == "yes":
        Game.get_current_weather()  # update weather

    # health: based on weather
    if Game.weather == "very hot":
        Player.health_points += 2
    elif Game.weather == "hot":
        Player.health_points += 1
    elif Game.weather == "cold":
        # add 0 if 2+ sets of clothing per person
        # add 2 if 0 sets of clothing per person
        # apply sliding scale between 0-2 sets per person
        sets_per_person = math.floor(Inventory.clothing / Player.persons_alive)
        if sets_per_person >= 2:
            Player.health_points += 0
        elif sets_per_person == 0:
            Player.health_points += 2
        else:
            Player.health_points += sets_per_person
    elif Game.weather == "very cold":
        # add 0 if 4+ sets of clothing per person
        # add 4 if 0 sets of clothing per person
        # apply sliding scale between 0-4 sets per person
        sets_per_person = math.floor(Inventory.clothing / Player.persons_alive)
        if sets_per_person >= 4:
            Player.health_points += 0
        elif sets_per_person == 0:
            Player.health_points += 4
        elif sets_per_person == 3:
            Player.health_points += 1
        elif sets_per_person == 2:
            Player.health_points += 2
        else:
            Player.health_points += 3

    # health: based on food rations
    if Inventory.food == 0:
        Player.health_points += 6
    elif Player.rations == "filling":
        Player.health_points += 0
    elif Player.rations == "meager":
        Player.health_points += 2
    elif Player.rations == "bear bones":
        Player.health_points += 4

    # health: based on pace
    if is_rest_day:
        Player.health_points += 0
    elif Player.pace == "steady":
        Player.health_points += 2
    elif Player.pace == "strenuous":
        Player.health_points += 4
    elif Player.pace == "grueling":
        Player.health_points += 6

    # update overall health based on health points value
    Player.update_health()

    if show_wagon:
        static_wagon(Game, Inventory, Player)

    # deduct food rations
    Inventory.food -= Player.rations_pounds_per_day
    if Inventory.food <= 0:
        # never get into negative food rations
        Inventory.food = 0

    if is_rest_day:
        # visualize daily increments on calendar (only if rest day)
        generate_title_date(green, current_location["name"], Game.date_string)
        print("")
        print(CENT(f"Stopping to Rest (day: {n+1})"))
        Game.add_one_day()  # increment the day +1
        time.sleep(1)
    elif is_trade_day:
        Game.add_one_day()  # increment the day +1
    else:
        # not a rest/trade day, so increment miles traveled
        Game.distance_traveled += Player.pace_miles_per_day
        # deduct miles until next destination
        Game.next_destination_distance -= Player.pace_miles_per_day
        if Game.next_destination_distance < 0:
            # if arriving before day's end,
            # get the absolute abs() value of remaining miles
            negative_miles = abs(Game.next_destination_distance)
            # set next destination hard-coded to 0 remaining
            Game.next_destination_distance = 0
            # deduct the abs() miles from total distance traveled
            Game.distance_traveled -= negative_miles

        Game.add_one_day()  # increment the day +1
        if show_wagon:
            time.sleep(1)


def stop_to_rest(Game, Inventory, Player):
    """
    Allows player to stop to rest between 1-9 day(s).
    Normal daily cycles/deductions resume.
    """
    while True:
        generate_title(green, "Stop to Rest")

        user_input = input(f"\t\tHow many days would you like to rest? {green('[1-9]')} ")  # noqa
        choices = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

        # validate if the user selected a valid option
        if validate_choice(user_input, choices):
            break

    # cycle the day 'n' number of times
    for n in range(0, int(user_input)):
        cycle_one_day(Game, Inventory, Player, True, False, True, n)


def attempt_to_trade(Game, Inventory, Player):
    """
    Using weighted ratios to calculate randomized trades.
    """
    # using weighted ratios, grab one of each wants/gender/gives
    wants = random.choices(trades.wants_choices, trades.want_weights)
    gender = random.choices(trades.gender_choices, trades.gender_weights)
    gives = random.choices(trades.gives_choices, trades.gives_weights)

    # only if someone does want to trade
    if wants[0]["item"] != "nobody":
        # make sure emigrant doesn't give back same thing they want
        while True:
            if gives[0]["inventory_name"] == wants[0]["inventory_name"]:
                gives = random.choices(trades.gives_choices, trades.gives_weights)  # noqa
            else:
                break

        # handle emigrant wanting random amounts of bullets/food
        if wants[0]["item"] == "bullets" or wants[0]["item"] == "pounds of food":  # noqa
            # 75% of the time, want 100-300 bullets/pounds of food
            # 25% of the time, want 301-400 bullets/pounds of food
            wants_qty_choices = [random.randint(301, 400), random.randint(100, 300)]  # noqa
            wants_qty_weights = [0.25, 0.75]
            wants[0]["qty"] = random.choices(wants_qty_choices, wants_qty_weights)[0]  # noqa
        wanted = f"""{wants[0]["qty"]} {wants[0]["item"]}"""

        # handle emigrant giving random amounts of bullets/food
        if gives[0]["item"] == "bullets" or gives[0]["item"] == "pounds of food":  # noqa
            # 75% of the time, gives 20-70 bullets/pounds of food
            # 25% of the time, want 71-100 bullets/pounds of food
            gives_qty_choices = [random.randint(71, 100), random.randint(20, 70)]  # noqa
            gives_qty_weights = [0.25, 0.75]
            gives[0]["qty"] = random.choices(gives_qty_choices, gives_qty_weights)[0]  # noqa
        trading = f"""{gives[0]["qty"]} {gives[0]["item"]}"""

    while True:
        generate_title(yellow, "Attempt to Trade: Your Supplies")
        print(f"\t\t\t{'oxen':<24}{Inventory.oxen}")
        time.sleep(0.05)
        print(f"\t\t\t{'sets of clothing':<24}{Inventory.clothing}")
        time.sleep(0.05)
        print(f"\t\t\t{'bullets':<24}{Inventory.bullets}")
        time.sleep(0.05)
        print(f"\t\t\t{'wagon wheels':<24}{Inventory.wheels}")
        time.sleep(0.05)
        print(f"\t\t\t{'wagon axles':<24}{Inventory.axles}")
        time.sleep(0.05)
        print(f"\t\t\t{'wagon tongues':<24}{Inventory.tongues}")
        time.sleep(0.05)
        print(f"\t\t\t{'pounds of food':<24}{Inventory.food}")
        time.sleep(0.05)
        print("")
        time.sleep(0.05)
        print(yellow(LINE))
        time.sleep(0.05)
        print("")
        time.sleep(0.05)

        # nobody wants to trade with you (20% of the time)
        if wants[0]["item"] == "nobody":
            print(CENT("No one wants to trade with you today."))
            time.sleep(0.05)
            print("")
            time.sleep(0.05)
            print(yellow(LINE))
            time.sleep(0.05)
            input(f'{grey(CENT("Press ENTER to continue"))}\n')
            break

        else:  # someone wants to trade
            print(CENT(f"""You meet another emigrant who wants {wanted}."""))
            time.sleep(0.05)

            # check to see if player has this in their inventory
            inv_name = wants[0]["inventory_name"]
            if int(wants[0]["qty"]) > int(Inventory[inv_name]):
                # player doesn't have enough to trade
                print(CENT("You don't have this."))
                time.sleep(0.05)
                print("")
                time.sleep(0.05)
                print(yellow(LINE))
                time.sleep(0.05)
                input(f'{grey(CENT("Press ENTER to continue"))}\n')
                break
            else:
                # player has enough to trade
                print(CENT(f"""{gender[0]} will trade you {trading}."""))
                time.sleep(0.05)
                print("")
                time.sleep(0.05)
                user_input = input(f"\n\t\tAre you willing to trade? {yellow('[yes/no]')} ")  # noqa

                # validate if the user selected a valid option
                if validate_yes_no(user_input):

                    # user does want to confirm this trade
                    if user_input[0].lower() == "y":
                        # inventory items to give/trade
                        inv_name_in = gives[0]["inventory_name"]
                        inv_name_out = wants[0]["inventory_name"]
                        # increment item being given
                        current_qty_in = Inventory[inv_name_in]
                        new_qty_in = int(current_qty_in) + int(gives[0]["qty"])
                        setattr(Inventory, inv_name_in, new_qty_in)
                        # decrement item being traded away
                        current_qty_out = Inventory[inv_name_out]
                        new_qty_out = int(current_qty_out) - int(wants[0]["qty"])  # noqa
                        setattr(Inventory, inv_name_out, new_qty_out)
                        # redisplay supplies
                        generate_title(yellow, "Attempt to Trade: Your Supplies")  # noqa
                        print(f"\t\t\t{'oxen':<24}{Inventory.oxen}")
                        print(f"\t\t\t{'sets of clothing':<24}{Inventory.clothing}")  # noqa
                        print(f"\t\t\t{'bullets':<24}{Inventory.bullets}")
                        print(f"\t\t\t{'wagon wheels':<24}{Inventory.wheels}")
                        print(f"\t\t\t{'wagon axles':<24}{Inventory.axles}")
                        print(f"\t\t\t{'wagon tongues':<24}{Inventory.tongues}")  # noqa
                        print(f"\t\t\t{'pounds of food':<24}{Inventory.food}")
                        print("")
                        print(yellow(LINE))
                        input(f'{grey(CENT("Press ENTER to continue"))}\n')
                        break
                    else:  # user does not want to trade
                        break

    # cycle a normal day (deduct food) without showing the static ox/wagon
    cycle_one_day(Game, Inventory, Player, False, True, False, 0)


def display_distance(current, miles, next):
    """
    Info screen to advise current destination, with
    the distance and name to the next destination
    """
    # display message about upcoming journey (name/distance)
    generate_title(yellow, "Continue on Trail")
    message = f"""
{CENT(f"From {current},")}
{CENT(f"it is {miles} miles")}
{CENT(f"to {next}.")}
    """  # noqa
    print(message)
    print("")
    print(yellow(LINE))
    input(f'{grey(CENT("Press ENTER to continue"))}\n')


def look_around(destination):
    """
    Info screen to announce arrival at next destination.
    Gives the option to look around, or not.
    """
    # display message about arrival destination (name/distance)
    while True:
        generate_title(yellow, "You have arrived")
        print(CENT(f"You are now at {destination}."))
        user_input = input(f"\n\t\tWould you like to look around? {yellow('[yes/no]')} ")  # noqa

        # validate if the user selected a valid option
        if validate_yes_no(user_input):
            break

    if user_input[0].lower() == "y":
        return True
    else:
        return False


def continue_on_trail(Game, Inventory, Player, current_location, next_destination_id):  # noqa
    """
    Player has left previous landmark, en route to next one.
    """
    pass


def buy_item(Game, Player, Inventory, item, cost, text, question, min, max):
    """
    Helper function to buy items at forts,
    or Independence, if the player hasn't left yet.
    """
    while True:
        generate_title_date(red, Game.current_location["name"], Game.date_string)  # noqa
        print(text)
        print(CENT(f"You have ${Player.cash:.2f} to spend."))
        print("")

        if max <= 0:
            # player cannot buy more of this supply
            print(CENT(f"You are already at the maximum number of {item}."))
            print("")
            print(red(LINE))
            input(f'{grey(CENT("Press ENTER to continue"))}\n')
            break

        item_qty = input(question)

        # validate if the user selected a valid option
        if validate_minmax(item_qty, min, max):

            if int(item_qty) == 0:
                break
            else:
                # ensure player can afford the full value
                total_cost = int(item_qty) * cost
                if Player.cash - total_cost >= 0:
                    # player has enough money remaining to make purchase

                    # deduct the payment from their cash
                    new_cash = Player.cash - total_cost
                    setattr(Player, "cash", new_cash)

                    # increment item, on top of any existing for this item
                    curr_inv_qty = getattr(Inventory, item)
                    if item == "bullets":
                        new_inv_qty = int(curr_inv_qty) + (int(item_qty) * 20)
                    else:
                        new_inv_qty = int(curr_inv_qty) + int(item_qty)
                    # update inventory amounts
                    setattr(Inventory, item, new_inv_qty)

                else:
                    # player cannot afford the full transaction
                    print(red(CENT(f"You cannot afford {item_qty} {item}")))
                    input(f'{grey(CENT("Press ENTER to continue"))}\n')

                break


def buy_supplies(Game, Inventory, Player):
    """
    Player is at a fort (or Independence still, after leaving Matt's).
    The option to buy [more] supplies is available.
    """
    current_location = Game.current_location
    cost_oxen = current_location["cost_oxen"]
    cost_food = current_location["cost_food"]
    cost_clothing = current_location["cost_clothing"]
    cost_bullets = current_location["cost_bullets"]
    cost_wagon_wheels = current_location["cost_wagon_wheels"]
    cost_wagon_axles = current_location["cost_wagon_axles"]
    cost_wagon_tongues = current_location["cost_wagon_tongues"]

    while True:
        generate_title_date(red, Game.current_location["name"], Game.date_string)  # noqa
        time.sleep(0.05)
        print("\t\tYou may buy:\n")
        time.sleep(0.05)
        print(f"\t\t\t{red('1. ') + 'Oxen':<60}{cost_oxen:.2f} per ox")
        time.sleep(0.05)
        print(f"\t\t\t{red('2. ') + 'Clothing':<60}{cost_clothing:.2f} per set")  # noqa
        time.sleep(0.05)
        print(f"\t\t\t{red('3. ') + 'Ammunition':<60} {cost_bullets:.2f} per box")  # noqa
        time.sleep(0.05)
        print(f"\t\t\t{red('4. ') + 'Wagon wheels':<60}{cost_wagon_wheels:.2f} per wheel")  # noqa
        time.sleep(0.05)
        print(f"\t\t\t{red('5. ') + 'Wagon axles':<60}{cost_wagon_axles:.2f} per axle")  # noqa
        time.sleep(0.05)
        print(f"\t\t\t{red('6. ') + 'Wagon tongues':<60}{cost_wagon_tongues:.2f} per tongue")  # noqa
        time.sleep(0.05)
        print(f"\t\t\t{red('7. ') + 'Food':<60} {cost_food:.2f} per pound")
        time.sleep(0.05)
        print(f"\t\t\t{red('8. ') + 'Leave Store'}")
        time.sleep(0.05)
        print(red(LINE))
        time.sleep(0.05)
        print(CENT(f"""You have ${Player.cash:>2.2f} to spend."""))
        time.sleep(0.05)

        user_input = input(f"\n\t\t\tWhich number? {red('[1-8]')} ")
        choices = ["1", "2", "3", "4", "5", "6", "7", "8"]

        # validate if the user selected a valid option
        if validate_choice(user_input, choices):

            if user_input == "1":  # oxen
                cost = cost_oxen
                curr_qty = Inventory.oxen
                max_qty = 20
                max_buy = max_qty - curr_qty
                text = (f"""
{CENT(f"You may only take {max_qty} oxen.")}
{CENT(f"Currently you have {Inventory.oxen}.")}
{CENT(f"That means you can buy a maximum of {max_buy}.")}

{CENT(f"Cost per ox: ${cost:.2f}")}""")
                question = f"\t\t\tHow many oxen? {red(f'[0-{max_buy}]')} "  # noqa
                buy_item(Game, Player, Inventory, "oxen", cost, text, question, 0, max_buy)  # noqa
            elif user_input == "2":  # clothing
                cost = cost_clothing
                curr_qty = Inventory.clothing
                max_qty = 200
                max_buy = max_qty - curr_qty
                text = (f"""
{CENT(f"You may only take {max_qty} sets of clothing.")}
{CENT(f"Currently you have {Inventory.clothing}.")}
{CENT(f"That means you can buy a maximum of {max_buy}.")}

{CENT(f"Cost per set: ${cost:.2f}")}""")
                question = f"\t\t\tHow many sets? {red(f'[0-{max_buy}]')} "  # noqa
                buy_item(Game, Player, Inventory, "clothing", cost, text, question, 0, max_buy)  # noqa
            elif user_input == "3":  # bullets
                cost = cost_bullets
                curr_qty = Inventory.bullets
                max_qty = 10000
                max_buy = int((max_qty - curr_qty) / 20)
                text = (f"""
{CENT(f"You may only take {max_qty} bullets.")}
{CENT(f"Currently you have {Inventory.bullets}.")}
{CENT(f"That means you can buy a maximum of {max_buy}.")}

{CENT(f"Cost per box: ${cost:.2f}")}""")
                question = f"\t\t\tHow many boxes? {red(f'[0-{max_buy}]')} "  # noqa
                buy_item(Game, Player, Inventory, "bullets", cost, text, question, 0, max_buy)  # noqa
            elif user_input == "4":  # wagon wheels
                cost = cost_wagon_wheels
                curr_qty = Inventory.wheels
                max_qty = 3
                max_buy = max_qty - curr_qty
                text = (f"""
{CENT(f"You may only take {max_qty} wagon wheels.")}
{CENT(f"Currently you have {Inventory.wheels}.")}
{CENT(f"That means you can buy a maximum of {max_buy}.")}

{CENT(f"Cost per wagon wheel: ${cost:.2f}")}""")
                question = f"\t\t\tHow many wheels? {red(f'[0-{max_buy}]')} "  # noqa
                buy_item(Game, Player, Inventory, "wheels", cost, text, question, 0, max_buy)  # noqa
            elif user_input == "5":  # wagon axles
                cost = cost_wagon_axles
                curr_qty = Inventory.axles
                max_qty = 3
                max_buy = max_qty - curr_qty
                text = (f"""
{CENT(f"You may only take {max_qty} wagon axles.")}
{CENT(f"Currently you have {Inventory.axles}.")}
{CENT(f"That means you can buy a maximum of {max_buy}.")}

{CENT(f"Cost per wagon axle: ${cost:.2f}")}""")
                question = f"\t\t\tHow many axles? {red(f'[0-{max_buy}]')} "  # noqa
                buy_item(Game, Player, Inventory, "axles", cost, text, question, 0, max_buy)  # noqa
            elif user_input == "6":  # wagon tongues
                cost = cost_wagon_tongues
                curr_qty = Inventory.tongues
                max_qty = 3
                max_buy = max_qty - curr_qty
                text = (f"""
{CENT(f"You may only take {max_qty} wagon tongues.")}
{CENT(f"Currently you have {Inventory.tongues}.")}
{CENT(f"That means you can buy a maximum of {max_buy}.")}

{CENT(f"Cost per wagon tongue: ${cost:.2f}")}""")
                question = f"\t\t\tHow many tongues? {red(f'[0-{max_buy}]')} "  # noqa
                buy_item(Game, Player, Inventory, "tongues", cost, text, question, 0, max_buy)  # noqa
            elif user_input == "7":  # food
                cost = cost_food
                curr_qty = Inventory.food
                max_qty = 2000
                max_buy = max_qty - curr_qty
                text = (f"""
{CENT(f"You may only take {max_qty} pounds of food.")}
{CENT(f"Currently you have {Inventory.food}.")}
{CENT(f"That means you can buy a maximum of {max_buy}.")}

{CENT(f"Cost per pound: ${cost:.2f}")}""")
                question = f"\t\t\tHow many pounds? {red(f'[0-{max_buy}]')} "  # noqa
                buy_item(Game, Player, Inventory, "food", cost, text, question, 0, max_buy)  # noqa
            elif user_input == "8":
                break


def river_crossing():
    """
    River crossing are an essential part of the game mechanics.
    There are variable outcomes, from uneventful, to completely deadly.
    """
    input("at river")


def start_cycle(Game, Inventory, Player):
    """
    Starts the main game play in Independence.
    """
    # handle new/existing chats to people
    talked_to_people = False
    convos = []

    current_location = Game.get_current_location()
    next_destination_id = current_location["next_destination_id"]
    Game.next_destination_distance = current_location["next_destination_distance"]  # noqa
    Game.get_current_weather()  # set the starter weather

    while True:
        generate_title_date(green, current_location["name"], Game.date_string)

        print(f"\t\t\t{'Weather:':<24}{Game.weather} ({Game.rand_temp}°F)")
        time.sleep(0.05)
        print(f"\t\t\t{'Health:':<24}{Player.health}")
        time.sleep(0.05)
        print(f"\t\t\t{'Pace:':<24}{Player.pace}")
        time.sleep(0.05)
        print(f"\t\t\t{'Rations:':<24}{Player.rations}")
        time.sleep(0.05)
        print(green(LINE))
        time.sleep(0.05)

        print("\tYou may:\n")
        time.sleep(0.05)
        print(f'\t\t{green("1. ")}{"Continue on trail"}')
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

            while True:  # used for "look around" looping

                clear()
                if user_input == "1":  # continue on trail
                    talked_to_people = False  # reset conversation shuffle
                    next_destination_distance = current_location["next_destination_distance"]  # noqa
                    current_pace = Player.pace_miles_per_day  # 18 || 30 || 36

                    # river crossings
                    if current_location["category"] == "river":
                        river_crossing()

                    # split paths along trail (GH Issue #3)
                    if type(current_location["next_destination_id"]) == list:
                        while True:
                            generate_title(yellow, "The trail divides here")
                            print("\tYou may:\n")
                            time.sleep(0.05)
                            print(f'\t\t{yellow("1. ")}{f"""head for {current_location["next_destination_name"][0]}"""}')  # noqa
                            time.sleep(0.05)
                            print(f'\t\t{yellow("2. ")}{f"""head for {current_location["next_destination_name"][1]}"""}')  # noqa
                            time.sleep(0.05)
                            print(f'\t\t{yellow("3. ")}{"see the map"}')
                            time.sleep(0.05)
                            user_input = input(f"\n\t\tWhat is your choice? {yellow('[1-3]')} ")  # noqa
                            time.sleep(0.05)
                            choices = ["1", "2", "3"]

                            # validate if the user selected a valid option
                            if validate_choice(user_input, choices):

                                if user_input == "1":
                                    next_destination_distance = current_location["next_destination_distance"][0]  # noqa
                                    days_required_to_next_destination = math.ceil(next_destination_distance / current_pace)  # noqa
                                    Game.next_destination_distance = current_location["next_destination_distance"][0]  # noqa
                                    display_distance(current_location["name"], Game.next_destination_distance, current_location["next_destination_name"][0])  # noqa
                                    # set next destination as current
                                    Game.current_location_id = next_destination_id[0]  # noqa
                                    current_location = Game.get_current_location()  # noqa
                                    next_destination_id = current_location["next_destination_id"]  # noqa
                                    break
                                elif user_input == "2":
                                    next_destination_distance = current_location["next_destination_distance"][1]  # noqa
                                    days_required_to_next_destination = math.ceil(next_destination_distance / current_pace)  # noqa
                                    Game.next_destination_distance = current_location["next_destination_distance"][1]  # noqa
                                    display_distance(current_location["name"], Game.next_destination_distance, current_location["next_destination_name"][1])  # noqa
                                    # set next destination as current
                                    Game.current_location_id = next_destination_id[1]  # noqa
                                    current_location = Game.get_current_location()  # noqa
                                    next_destination_id = current_location["next_destination_id"]  # noqa
                                    break
                                elif user_input == "3":
                                    show_map()
                    else:
                        # one option only, no split path
                        days_required_to_next_destination = math.ceil(next_destination_distance / current_pace)  # noqa
                        display_distance(current_location["name"], next_destination_distance, current_location["next_destination_name"])  # noqa
                        # set next destination as current
                        Game.current_location_id = next_destination_id
                        current_location = Game.get_current_location()
                        next_destination_id = current_location["next_destination_id"]  # noqa

                    # cycle one day per required day to the next destination
                    for n in range(0, days_required_to_next_destination):
                        clear()
                        cycle_one_day(Game, Inventory, Player, False, False, True, n)  # noqa
                    animate_wagon(Game, Inventory, Player)

                    # reset distance to next destination
                    Game.next_destination_distance = current_location["next_destination_distance"]  # noqa

                    # destination is not the end/Oregon
                    if current_location["category"] != "end":
                        # arrived at next destination - look around?
                        look = look_around(Game.current_location["name"])
                        if not look:
                            # skip stopping at this destination
                            continue
                        else:
                            # have a look at this destination
                            break
                    else:
                        # reached Oregon!
                        # TODO: needs to break out of outer loop also!!!
                        break

                elif user_input == "2":  # check supplies
                    check_supplies(Inventory, Player)
                    break

                elif user_input == "3":  # look at map
                    show_map()
                    break

                elif user_input == "4":  # change pace
                    change_pace(Player)
                    break

                elif user_input == "5":  # change food rations
                    change_ration(Player)
                    break

                elif user_input == "6":  # stop to rest
                    stop_to_rest(Game, Inventory, Player)
                    break

                elif user_input == "7":  # attempt to trade
                    attempt_to_trade(Game, Inventory, Player)
                    break

                elif user_input == "8":  # talk to people

                    # first time talking to people, randomize conversations
                    if not talked_to_people:
                        convos = []  # reset
                        shuffle_conversations = Game.shuffle_conversations(current_location["conversations"])  # noqa
                        talked_to_people = True
                        convos.extend(shuffle_conversations)

                    generate_title(pink, f"Talking to {convos[0]['person']}")
                    print(CENT(convos[0]["speech"]))
                    print("")
                    print(pink(LINE))
                    input(f'{grey(CENT("Press ENTER to continue"))}\n')
                    Game.talk_to_people(convos)  # pop + append convo to end
                    break

                elif user_input == "9":  # buy supplies
                    buy_supplies(Game, Inventory, Player)
                    break
